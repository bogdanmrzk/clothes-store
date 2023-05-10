# Generated by Django 4.1.7 on 2023-04-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_productsize_size'),
        ('cart', '0006_remove_order_items_remove_orderitems_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='cart.OrderItems', to='products.products'),
        ),
    ]
