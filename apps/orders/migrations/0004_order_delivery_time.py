# Generated by Django 5.0.6 on 2024-05-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_distance_function'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
