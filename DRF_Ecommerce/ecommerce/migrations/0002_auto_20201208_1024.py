# Generated by Django 3.1.4 on 2020-12-08 10:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gallery',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), size=None),
        ),
    ]
