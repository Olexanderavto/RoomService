# Generated by Django 5.2.4 on 2025-07-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_category_options_roomimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='category_photos/'),
        ),
    ]
