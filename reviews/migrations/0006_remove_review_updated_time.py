# Generated by Django 4.2.10 on 2024-03-23 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0005_remove_comment_updated_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="updated_time",
        ),
    ]