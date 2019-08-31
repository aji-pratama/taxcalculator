from django.contrib import admin
from taxcalculator import models as taxcalculator_models


@admin.register(taxcalculator_models.Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['name', 'tax_code', 'refundable', 'price', 'tax', 'amount']
