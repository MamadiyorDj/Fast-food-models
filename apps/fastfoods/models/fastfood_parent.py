from django.db import models
from .fastfoods import FastFood
from apps.products.models.products import Product
# Create your models here.


class FastFoodParent(models.Model):
    id = models.AutoField(primary_key=True)
    fastfood = models.ForeignKey(FastFood, on_delete=models.CASCADE, related_name='fastfood')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fastfoodparent')

    def __str__(self):
        return self.fastfood.name

    class Meta:
        ordering = ['-id']