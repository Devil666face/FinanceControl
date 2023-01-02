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
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from Finance.models import (
    Order, 
    Category, 
    Image, 
    Report
)
from Finance.forms import (
    CategoryCreateForm,
)
from Finance.mixin import (
    LoginMixin,
    OrderMixin,
    ReportMixin,
)
from Finance.utils import (
    get_now_month,
    get_first_last_date_for_month,
    remove_old_report,
    get_totals,
)
from Finance.forms import (
    OrderCreateForm,
    ReportCreateForm
)
from Finance.filter import OrderFilter
from Finance.report import ReportMaker


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
        print(first_day, last_day)
        context['filter'] = OrderFilter(self.request.GET, queryset=Order.objects.filter(created_at__gte=first_day, created_at__lte=last_day))
        context['order_list'] = context['filter'].qs
        context['report'] = ReportCreateForm()
        return context


class OrderDetailView(OrderMixin, DetailView):
    pass


class OrderCreateView(OrderMixin, CreateView):
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


class OrderUpdateView(OrderMixin, UpdateView):
    form_class = OrderCreateForm


class OrderDeleteView(OrderMixin, DeleteView):
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.delete(request, *args, **kwargs)
        return redirect(request.META.get('HTTP_REFERER','/'))


class CategoryDetailView(LoginMixin, DetailView):
    pass


class CategoryCreateView(LoginMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'form.html'
    success_url = reverse_lazy('order_list')


class ReportCreateView(ReportMixin, CreateView):
    form_class = ReportCreateForm

    def get_success_url(self):
        return reverse_lazy('report_pdf',kwargs={'slug':self.object.slug})   

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        self.date_month = request.POST.get('date_month')+'-01'
        request.POST['date_month']=self.date_month
        request.POST._mutable = False
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.report_object = ReportMaker(self.object)
        self.object = self.report_object.get_obj()
        if self.report_object.queryset:
            self.object.save()
            return super().form_valid(form)
        else:
            form.add_error(None,'Orders for current month not found')
            return super().form_invalid(form)


class ReportDetailViewPdf(ReportMixin, DetailView):

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return HttpResponse(self.object.file, content_type="application/pdf")


class ReportListView(ReportMixin, ListView):
    template_name = 'report_list'

    def get_queryset(self):
        self.queryset = super().get_queryset()
        if self.queryset:
            self.revenue, self.expend, self.balance = get_totals(self.queryset)
        # self.queryset = Report.objects.filter(slug='12312312asddqw').all()
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.queryset:
            context['revenue'] = self.revenue
            context['expend'] = self.expend
            context['balance'] = self.balance
        return context


class ReportDetailView(ReportMixin, DetailView):
    template_name = 'report_detail'


class ReportDeleteView(ReportMixin, DeleteView):

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.delete(request, *args, **kwargs)
        # return redirect(request.META.get('HTTP_REFERER','/'))
        return HttpResponse('')
