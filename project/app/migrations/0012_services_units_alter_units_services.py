# Generated by Django 5.0.7 on 2024-08-01 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0011_remove_services_units_units_services"),
    ]

    operations = [
        migrations.AddField(
            model_name="services",
            name="units",
            field=models.ManyToManyField(
                blank=True,
                related_name="units_set",
                related_query_name="unit",
                to="app.units",
            ),
        ),
        migrations.AlterField(
            model_name="units",
            name="services",
            field=models.ManyToManyField(
                blank=True,
                related_name="services_set",
                related_query_name="service",
                to="app.services",
            ),
        ),
    ]
