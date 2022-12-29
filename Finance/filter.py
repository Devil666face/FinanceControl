import django_filters
from django import forms
from django_filters import CharFilter, ModelMultipleChoiceFilter
from Finance.models import Order, Category


class OrderFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title:')    
    category = ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, label='Category:')
    
    class Meta:
        model = Order
        fields = ['title', 'category']