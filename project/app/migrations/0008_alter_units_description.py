# Generated by Django 5.0.7 on 2024-07-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_units_politices_data_services"),
    ]

    operations = [
        migrations.AlterField(
            model_name="units",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
