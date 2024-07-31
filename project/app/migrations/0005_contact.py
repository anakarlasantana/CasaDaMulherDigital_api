# Generated by Django 5.0.7 on 2024-07-31 01:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_rename_politics_politices"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
    ]
