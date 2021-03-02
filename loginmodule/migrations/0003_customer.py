# Generated by Django 3.1.5 on 2021-03-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginmodule', '0002_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
