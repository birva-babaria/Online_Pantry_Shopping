# Generated by Django 3.1.5 on 2021-03-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingmodule', '0005_auto_20210303_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]
