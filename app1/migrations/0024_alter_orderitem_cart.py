# Generated by Django 4.2.2 on 2024-03-01 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_alter_orderitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='app1.cart'),
        ),
    ]
