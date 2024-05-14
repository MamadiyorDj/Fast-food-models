from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.account.models.users import User
from apps.fastfoods.models.fastfoods import FastFood
from apps.orders.models.order_items import OrderItem

# Create your models here.


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    fastfood = models.ForeignKey(FastFood, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    delivery_address = models.CharField(max_length=150, blank=True)
    delivery_phone = PhoneNumberField(blank=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=13)
    longitude = models.DecimalField(max_digits=17, decimal_places=13)
    order_items = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='order')
    total = models.IntegerField(default=0, blank=True)
    delivery_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-id']