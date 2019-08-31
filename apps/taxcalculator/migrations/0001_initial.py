# Generated by Django 2.1.5 on 2019-08-31 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('tax_code', models.PositiveSmallIntegerField(choices=[(1, 'food'), (2, 'tobacco'), (3, 'entertainment')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
    ]
