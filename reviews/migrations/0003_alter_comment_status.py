# Generated by Django 4.2.10 on 2024-03-20 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]
