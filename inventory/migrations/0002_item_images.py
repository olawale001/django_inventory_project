# Generated by Django 5.0.7 on 2024-08-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='images',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
