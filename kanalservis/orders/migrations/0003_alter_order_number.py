# Generated by Django 4.1.1 on 2022-09-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_order_number_alter_order_supply_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.PositiveSmallIntegerField(),
        ),
    ]