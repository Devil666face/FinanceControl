from Finance.utils import get_first_last_date_for_month
from Finance.models import Order, Category
from datetime import datetime
from django.shortcuts import render
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa


class Render:
	def __init__(self, template, context:dict):
		template = get_template(template)
		self.html = template.render(context)
		self.result = BytesIO()
		self.pdf = pisa.pisaDocument(BytesIO(self.html.encode("ISO-8859-1")), self.result)

	def get_pdf(self):
		if not self.pdf.err:
			return HttpResponse(self.result.getvalue(), content_type="application/pdf")


class ReportMaker:
	def __init__(self, obj):
		self.obj = obj
		current_month = str(self.obj.date_month).split('-')[1]
		self.obj.title = self._get_title(current_month)
		self.queryset = self._get_queryset(current_month)
		self.table_for_record = self._make_table_for_record()
		self.average_dict = self._count_average()
		self.percent_of_revenue = self._count_percent()
		print(self.average_dict)

	def _count_percent(self):
		revenue = self.average_dict['Revenue']
		for cat_key in self.average_dict:
			percent = abs(self.average_dict[cat_key]/revenue)*100
			print(percent)
		
	def _count_average(self):
		current_category_list = set([order.category for order in self.queryset])
		average_dict = {category:0 for category in current_category_list}
		balance, revenue, expend = 0, 0, 0
		for order in self.queryset:
			sum_now = average_dict[order.category] + order.count
			average_dict[order.category] = sum_now
			balance = balance + order.count
			if order.count < 0:
				expend = expend + order.count
			else:
				revenue = revenue + order.count
		average_dict['Balance'] = balance
		average_dict['Revenue'] = revenue
		average_dict['Expend'] = expend
		return average_dict
	
	def _make_table_for_record(self):

		def _get_row(order):
			return [order.created_at.strftime('%Y-%m-%d %H:%M'), order.title, order.count, order.category.title]
		
		table_for_record = [_get_row(order) for order in self.queryset]
		return table_for_record
			
	def _get_queryset(self, current_month):
		first_day, last_day = get_first_last_date_for_month(current_month)
		return Order.objects.filter(created_at__gte=first_day, created_at__lte=last_day).order_by('created_at').select_related('category')
		
	def _get_title(self, current_month):
	    return f'{datetime(datetime.today().year, int(current_month), 1).strftime("%B")} {datetime.today().year}'

	def get_obj(self):
		return self.obj