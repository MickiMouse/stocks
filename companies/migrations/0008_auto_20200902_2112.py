# Generated by Django 3.1.1 on 2020-09-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0007_auto_20200902_2106"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="place",
            name="stocks",
        ),
        migrations.RemoveField(
            model_name="stock",
            name="company",
        ),
        migrations.AddField(
            model_name="stock",
            name="places",
            field=models.ManyToManyField(
                blank=True, related_name="stocks", to="companies.Place"
            ),
        ),
    ]
