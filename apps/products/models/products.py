from django.db import models
from .categories import Category

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='uploads')
    price = models.IntegerField(default=0)
    description = models.TextField()
    active = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']