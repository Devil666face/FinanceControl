from django.template import Library
from datetime import datetime
from Finance.models import Image

register = Library()


@register.inclusion_tag('include/_navbar.html')
def show_navbar(request):
    current_page = request.get('PATH_INFO')
    return {'current_page': current_page}


@register.inclusion_tag('Finance/include/_paginator.html')
def show_paginator(current_month):    
    current_month = int(current_month)
    month_list = list()
    if current_month < int(datetime.today().month):
        month_list = [current_month+1, current_month, current_month-1]
    else:
        month_list = [month for month in range(current_month, current_month-3, -1)]
    return {'month_list': month_list, 'current_month': current_month}


@register.simple_tag(name='get_str_month')
def get_str_month(month_number):
    return datetime(datetime.today().year, month_number, 1).strftime("%B")


@register.inclusion_tag('Finance/include/_carousel.html')
def show_carousel(order, order_id):
    # image_list = Image.objects.filter(order=order)
    image_list = order.images.all()
    return {'image_list':image_list, 'order_id':order_id}