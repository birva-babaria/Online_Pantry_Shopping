# Generated by Django 3.1.5 on 2021-03-06 15:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginmodule', '0003_customer'),
        ('shoppingmodule', '0006_auto_20210305_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('orderdate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('order_cust_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loginmodule.customer')),
            ],
        ),
        migrations.CreateModel(
            name='orderitems',
            fields=[
                ('orderitems_id', models.AutoField(primary_key=True, serialize=False)),
                ('orderitems_order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoppingmodule.order')),
                ('orderitems_prod_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoppingmodule.product')),
            ],
        ),
    ]
