# Generated by Django 5.0.6 on 2024-05-13 05:06

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fastfoods', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='products.product')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('delivery_address', models.CharField(blank=True, max_length=150)),
                ('delivery_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('latitude', models.DecimalField(decimal_places=13, max_digits=17)),
                ('longitude', models.DecimalField(decimal_places=13, max_digits=17)),
                ('total', models.IntegerField(blank=True, default=0)),
                ('fastfood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastfoods.fastfood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('order_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.orderitem')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
