from django.db import models


# Create your models here.

class Stock(models.Model):
    category_opt = models.CharField(max_length=100)
    size_opt = models.CharField(max_length=10)
    item_code = models.CharField(max_length=100)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    margin_val = models.DecimalField(max_digits=10, decimal_places=2)
    stock_date = models.DateTimeField()

    class Meta:
        db_table = 'bbb_stock'
        verbose_name = 'bbb_stock'
        verbose_name_plural = 'bbb_stock'

    def __str__(self):
        return self.category_opt
