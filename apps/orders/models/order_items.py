from django.db import models
from apps.products.models.products import Product
# Create your models here.


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, blank=True)
    quantity = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.product.name

    class Meta:
        ordering = ['-id']