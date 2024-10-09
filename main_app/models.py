from django.db import models

from django.db import models

class CurrencyRate(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса курса валют')
    rate = models.DecimalField(max_digits=12, decimal_places=6, verbose_name='Курс валюты')
    currency_from = models.CharField(max_length=5, verbose_name='Код переводимой валюты')
    currency_to = models.CharField(max_length=5, verbose_name='Код получаемой валюты')

    def __str__(self):
        return f'{self.rate} - {self.currency}'

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'

