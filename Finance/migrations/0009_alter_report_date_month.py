# Generated by Django 4.1.4 on 2022-12-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0008_alter_report_options_rename_date_report_date_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date_month',
            field=models.DateTimeField(verbose_name='Date'),
        ),
    ]
