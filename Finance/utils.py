import calendar
from datetime import datetime
from Finance.models import Report

def get_now_month():
    return datetime.today().strftime('%m')

def get_first_last_date_for_month(current_month, **kwargs):
    current_month = int(current_month)
    today = datetime.today()
    first_date = datetime(kwargs.get('current_year',today.year), current_month, 1, 0, 0, 0)
    last_date = datetime(kwargs.get('current_year',today.year), current_month,
                         calendar.monthrange(today.year, current_month)[1], 23, 59, 59)
    return first_date, last_date

def remove_old_report(object):
    if Report.objects.get(slug=object.slug):
        Report.objects.get(slug=object.slug).delete()
        return True
    return False

def get_totals(queryset):
    revenue = 0
    expend = 0
    balance = 0
    for report in queryset:
        revenue = revenue + report.revenue
        expend = expend + report.expend
        balance = balance + report.balance
    return revenue, expend, balance

# def get_now_first_day_of_month():
#     today = datetime.today()
#     date = datetime(today.year, today.month, 1)
#     return date.strftime('%Y-%m-%d')
    