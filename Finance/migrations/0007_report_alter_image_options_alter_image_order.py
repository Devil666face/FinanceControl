# Generated by Django 4.1.4 on 2022-12-28 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0006_alter_category_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Title')),
                ('file', models.FileField(upload_to='report/%Y/%m/%d/', verbose_name='Report file')),
                ('date', models.DateField(verbose_name='Date')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['pk']},
        ),
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Finance.order', verbose_name='Order'),
        ),
    ]
