# Generated by Django 3.1.1 on 2020-09-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0002_auto_20200902_1930"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="stock",
            field=models.ManyToManyField(
                blank=True, related_name="addresses", to="companies.Stock"
            ),
        ),
    ]
