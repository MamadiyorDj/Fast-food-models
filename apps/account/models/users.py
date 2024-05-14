from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True)
    status = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    birth_date = models.DateTimeField(auto_now_add=True)
    Users_role = {
        "S": "Super admin",
        "O": "Ofitsiant",
        "U": "User",
    }
    user_role = models.CharField(max_length=1, choices=Users_role, default="U")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']