# Generated by Django 4.2.10 on 2024-03-23 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0006_remove_review_updated_time"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Anime",
        ),
    ]
