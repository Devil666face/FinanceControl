from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Finance.models import (
    Order, 
    Category, 
    Report
)
from Finance.forms import (
    OrderCreateForm,
    ReportCreateForm,
)
from django.views.generic import (
    FormView,
    View,
)
from django.urls import reverse_lazy


class LoginMixin(LoginRequiredMixin):
    login_url = '/login/'


class OrderMixin(LoginMixin, FormView):
    model = Order
    template_name = 'form.html'
    success_url = reverse_lazy('order_list')

class ReportMixin(LoginMixin, View):
    model = Report
    success_url = reverse_lazy('report_list')
    template_name = 'form.html'
   