# Generated by Django 2.1.5 on 2019-08-31 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxcalculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='price',
            field=models.FloatField(),
        ),
    ]