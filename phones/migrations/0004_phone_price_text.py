# Generated by Django 3.1.4 on 2021-01-22 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20210122_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='price_text',
            field=models.TextField(default='0'),
        ),
    ]
