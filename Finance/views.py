from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import (
    DetailView,
    ListView,
    FormView,
    UpdateView,
    CreateView,
    DeleteView,
    RedirectView
)
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from Finance.models import (
    Order, 
    Category, 
    Image, 
    Report
)
from Finance.forms import (
    UserLoginForm,
    CategoryCreateForm,
)
from Finance.mixin import (
    LoginMixin,
    OrderMixin,
)
from Finance.utils import (
    get_now_month,
    get_first_last_date_for_month,
    remove_old_report,
)
from Finance.forms import (
    OrderCreateForm,
    ReportCreateForm
)
from Finance.filter import OrderFilter
from Finance.report import ReportMaker
from config.settings import DEBUG


class UserLogin(LoginView):
    authentication_form = UserLoginForm
    template_name = 'Finance/login.html'
    redirect_authenticated_user = True
    next_page = '/'


class UserLogout(LogoutView):
    next_page = '/login/'


class PasswordChangeView(PasswordChangeView):
    pass


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'Finance/template_replace.html'
    next_page = '/'


class OrderListView(LoginMixin, ListView):
    model = Order
    template_name = 'Finance/order_list.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.current_month = request.GET.get('month', get_now_month())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['current_month'] = self.current_month
        context['form'] = OrderCreateForm()
        first_day, last_day = get_first_last_date_for_month(self.current_month)
        context['filter'] = OrderFilter(self.request.GET, queryset=Order.objects.filter(created_at__gte=first_day, created_at__lte=last_day))
        context['order_list'] = context['filter'].qs
        context['report'] = ReportCreateForm()
        return context

    # def get_queryset(self):
    #     first_day, last_day = get_first_last_date_for_month(self.current_month)
    #     return Order.objects.filter(created_at__gte=first_day, created_at__lte=last_day)


class OrderDetailView(LoginMixin, DetailView):
    pass


class OrderCreateView(LoginMixin, OrderMixin, CreateView):
    form_class = OrderCreateForm

    def post(self, request, *args, **kwargs):
        self.image = request.FILES.getlist('image')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form) -> HttpResponse:
        self.object = form.save(commit=False)
        if self.image:
            self.object.has_image=True
        self.object.save()
        for picture in self.image:
            Image.objects.create(order=self.object, image=picture).save()
        return super().form_valid(form)


class OrderUpdateView(LoginMixin, OrderMixin, UpdateView):
    form_class = OrderCreateForm


class OrderDeleteView(LoginMixin, OrderMixin, DeleteView):
    
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.delete(request, *args, **kwargs)
        return redirect(request.META.get('HTTP_REFERER','/'))


class CategoryDetailView(LoginMixin, DetailView):
    pass


class CategoryCreateView(LoginMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('order_list')


class ReportCreateView(LoginMixin, CreateView):
    model = Report
    form_class = ReportCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('order_list')

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        self.date_month = request.POST.get('date_month')+'-01'
        request.POST['date_month']=self.date_month
        request.POST._mutable = False
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object = ReportMaker(self.object).get_obj()
        self.object.save()
        return super().form_valid(form)
        