# Generated by Django 4.2.2 on 2024-02-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_rename_crt_cartitem_cart_order_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='catrpro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]