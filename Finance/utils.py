import calendar
from datetime import datetime
from Finance.models import Report

def get_now_month():
    return datetime.today().strftime('%m')

def get_first_last_date_for_month(current_month):
    current_month = int(current_month)
    today = datetime.today()
    first_date = datetime(today.year, current_month, 1, 0, 0, 0)
    last_date = datetime(today.year, current_month,
                         calendar.monthrange(today.year, current_month)[1], 23, 59, 59)
    return first_date, last_date

def remove_old_report(object):
    if Report.objects.get(slug=object.slug):
        Report.objects.get(slug=object.slug).delete()
        return True
    return False
    
# def get_now_first_day_of_month():
#     today = datetime.today()
#     date = datetime(today.year, today.month, 1)
#     return date.strftime('%Y-%m-%d')
    