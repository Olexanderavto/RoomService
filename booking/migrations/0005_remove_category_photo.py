# Generated by Django 5.2.4 on 2025-07-15 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_category_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='photo',
        ),
    ]
