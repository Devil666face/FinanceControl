from django.contrib import admin
from Finance.models import Order, Category, Report
from django.utils.safestring import mark_safe


class ModelAdmin(admin.ModelAdmin):
    field = '__all__'
    search_fields = ('title',)


class OrderAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'count', 'category', )
    list_editable = ('count', 'category', )
    list_filter = ('created_at', 'category', )


class CategoryAdmin(ModelAdmin):
    pass


class ReportAdmin(ModelAdmin):
    field = ('title', 'file', 'date_month')

    
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Report, ReportAdmin)

