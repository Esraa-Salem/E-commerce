# Generated by Django 4.2.2 on 2024-03-01 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_remove_orderitem_name_remove_orderitem_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='alaa',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='esraa',
            field=models.CharField(default='', max_length=500),
        ),
    ]
