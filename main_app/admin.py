from django.contrib import admin

from main_app.models import CurrencyRate


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('date', 'rate', 'currency_from', 'currency_to')