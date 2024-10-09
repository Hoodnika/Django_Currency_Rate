# Generated by Django 5.1.1 on 2024-10-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_currencyrate_rate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currencyrate',
            options={'verbose_name': 'Курс валюты', 'verbose_name_plural': 'Курсы валют'},
        ),
        migrations.AddField(
            model_name='currencyrate',
            name='currency_from',
            field=models.CharField(default='USD', max_length=5, verbose_name='Код переводимой валюты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currencyrate',
            name='currency_to',
            field=models.CharField(default='USD', max_length=5, verbose_name='Код получаемой валюты'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса курса валют'),
        ),
        migrations.AlterField(
            model_name='currencyrate',
            name='rate',
            field=models.DecimalField(decimal_places=6, max_digits=12, verbose_name='Курс валюты'),
        ),
    ]
