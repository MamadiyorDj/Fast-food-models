from django.db import models

# Create your models here.


class FastFood(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    latitude = models.DecimalField(max_digits=17, decimal_places=13, blank=True, null=True)
    longitude = models.DecimalField(max_digits=17, decimal_places=13, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
