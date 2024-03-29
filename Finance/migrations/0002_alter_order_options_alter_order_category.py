# Generated by Django 4.1.4 on 2022-12-26 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finance.category', verbose_name='Категория'),
        ),
    ]
