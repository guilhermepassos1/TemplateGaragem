# Generated by Django 5.0.6 on 2024-07-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_acessorio"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
    ]
