# Generated by Django 3.1.4 on 2021-01-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20210122_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(allow_unicode=True, verbose_name='slug'),
        ),
    ]