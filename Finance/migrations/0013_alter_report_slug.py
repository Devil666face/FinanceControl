# Generated by Django 4.1.4 on 2022-12-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0012_alter_report_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]
