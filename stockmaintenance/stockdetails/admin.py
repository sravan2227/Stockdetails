from django.contrib import admin
from .models import Stock


# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ('category_opt', 'size_opt', 'item_code', 'stock_date')


admin.site.register(Stock, StockAdmin)
