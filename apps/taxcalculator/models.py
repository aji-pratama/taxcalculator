from django.db import models


class Bill(models.Model):
    TAX_CODE_CHOICES = (
        (1, 'food'),
        (2, 'tobacco'),
        (3, 'entertainment')
    )

    name = models.CharField(max_length=254)
    tax_code = models.PositiveSmallIntegerField(choices=TAX_CODE_CHOICES)
    price = models.FloatField()

    def __str__(self):
        return self.name

    def tax_type(self):
        tax_code = {
            1: 'Food & Beverage',
            2: 'Tobacco',
            3: 'Entertainment'
        }
        return tax_code[self.tax_code]

    def refundable(self):
        return 'Yes' if self.tax_code == 1 else 'No'

    def tax(self):
        tax = {
            1: self._food_tax(),
            2: self._tobacco_tax(),
            3: self._entertainment_tax()
        }
        return tax[self.tax_code]

    def amount(self):
        if self.tax_code == 1:
            return self.price + self._food_tax()
        elif self.tax_code == 2:
            return self.price + self._tobacco_tax()
        elif self.tax_code == 3:
            return self.price + self._entertainment_tax()
        else:
            return None

    def _food_tax(self):
        return (10/100) * self.price

    def _tobacco_tax(self):
        return 10 + (2/100 * self.price)

    def _entertainment_tax(self):
        if 0 < self.price and self.price < 100:
            return 0
        return (1/100) * (self.price - 100)
