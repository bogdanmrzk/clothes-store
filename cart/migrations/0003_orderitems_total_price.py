# Generated by Django 4.1.7 on 2023-04-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
