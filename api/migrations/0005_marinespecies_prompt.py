# Generated by Django 5.1.4 on 2025-01-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_marinespecies_image_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="marinespecies",
            name="prompt",
            field=models.TextField(blank=True, null=True),
        ),
    ]
