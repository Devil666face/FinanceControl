from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Finance.models import Order, Category
from Finance.forms import (
    OrderCreateForm,
)
from django.views.generic import (
    FormView,
)
from django.urls import reverse_lazy


class LoginMixin(LoginRequiredMixin):
    login_url = '/login/'


class OrderMixin(FormView):
    model = Order
    template_name = 'form.html'
    success_url = reverse_lazy('order_list')
