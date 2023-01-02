from django.urls import path
from Finance.views import *


order = [
    path('', OrderListView.as_view(), name='order_list'),
    # path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
    path('order/create/', OrderCreateView.as_view(), name='create_order'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='update_order'),
    path('order/<int:pk>/delete', OrderDeleteView.as_view(), name='delete_order'),
]


category = [
    path('category/create/', CategoryCreateView.as_view(), name='create_category'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category'),
]


report = [
    path('report/create/', ReportCreateView.as_view(), name='create_report'),
    path('report/', ReportListView.as_view(), name='report_list'),
    path('report/<slug:slug>', ReportDetailView.as_view(), name='report'),
    path('report/<slug:slug>/pdf', ReportDetailViewPdf.as_view(), name='report_pdf'),
]


utils = [
    
]


urlpatterns = [
    *order,
    *category,
    *report,
]
