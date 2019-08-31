from django.test import TestCase
from taxcalculator.models import Bill


class BillTestCase(TestCase):
    def setUp(self):
        Bill.objects.create(name="Lucky Stretch", tax_code=2, price=1000)
        Bill.objects.create(name="Big Mac", tax_code=1, price=1000)
        Bill.objects.create(name="Movie", tax_code=3, price=150)

    def test_bill_tax_type(self):
        lucky = Bill.objects.get(name="Lucky Stretch")
        big = Bill.objects.get(name="Big Mac")
        movie = Bill.objects.get(name="Movie")
        self.assertEqual(lucky.tax_type(), 'Tobacco')
        self.assertEqual(big.tax_type(), 'Food & Beverage')
        self.assertEqual(movie.tax_type(), 'Entertainment')

    def test_bill_refundable(self):
        lucky = Bill.objects.get(name="Lucky Stretch")
        big = Bill.objects.get(name="Big Mac")
        movie = Bill.objects.get(name="Movie")
        self.assertEqual(lucky.refundable(), 'No')
        self.assertEqual(big.refundable(), 'Yes')
        self.assertEqual(movie.refundable(), 'No')

    def test_bill_tax(self):
        lucky = Bill.objects.get(name="Lucky Stretch")
        big = Bill.objects.get(name="Big Mac")
        movie = Bill.objects.get(name="Movie")
        self.assertEqual(lucky.tax(), 30.0)
        self.assertEqual(big.tax(), 100.0)
        self.assertEqual(movie.tax(), 0.5)

    def test_bill_amount(self):
        lucky = Bill.objects.get(name="Lucky Stretch")
        big = Bill.objects.get(name="Big Mac")
        movie = Bill.objects.get(name="Movie")
        self.assertEqual(lucky.amount(), 1030.0)
        self.assertEqual(big.amount(), 1100.0)
        self.assertEqual(movie.amount(), 150.5)
