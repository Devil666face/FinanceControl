# Generated by Django 4.1.4 on 2022-12-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0013_alter_report_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]