## Documentation

#### Running projects:

`$docker-compose up`



#### API  

###### 1. GET all tax: 

Url: `localhost:8000/api/v1/tax/`

Its will return data like this:

```
{
    "meta": {
        "limit": 20,
        "next": null,
        "offset": 0,
        "previous": null,
        "total_count": 3
    },
    "objects": [
        {
            "amount": 1030.0,
            "name": "Lucky Stretch",
            "price": 1000.0,
            "refundable": "No",
            "resource_uri": "/api/v1/tax/1/",
            "tax": 30.0,
            "tax_code": 2,
            "tax_type": "Tobacco"
        },
        {
            "amount": 1100.0,
            "name": "Big Mac",
            "price": 1000.0,
            "refundable": "Yes",
            "resource_uri": "/api/v1/tax/2/",
            "tax": 100.0,
            "tax_code": 1,
            "tax_type": "Food & Beverage"
        },
        {
            "amount": 150.5,
            "name": "Movie",
            "price": 150.0,
            "refundable": "No",
            "resource_uri": "/api/v1/tax/3/",
            "tax": 0.5,
            "tax_code": 3,
            "tax_type": "Entertainment"
        }
    ]
}
```



###### 2. GET detail tax: 

Url: `localhost:8000/api/v1/tax/{id}/`

Its will return data like this:

```
{
    "amount": 1100.0,
    "id": 2,
    "name": "Big Mac",
    "price": 1000.0,
    "refundable": "Yes",
    "resource_uri": "/api/v1/tax/2/",
    "tax": 100.0,
    "tax_code": 1,
    "tax_type": "Food & Beverage"
}
```

##### 

##### 3. [POST] Tax:

url : `localhost:8000/api/v1/tax/`

Example body post :

```
{
	"name": "Mencoba",
	"tax_code": 1,
	"price": 2000
}
```



## DB Design

As on test docs, the DB design is only save `name`, `tax_code`, and `amount`, so DB design is as on project ORM  django models:

```
class Bill(models.Model):
    TAX_CODE_CHOICES = (
        (1, 'food'),
        (2, 'tobacco'),
        (3, 'entertainment')
    )

    name = models.CharField(max_length=254)
    tax_code = models.PositiveSmallIntegerField(choices=TAX_CODE_CHOICES)
    price = models.FloatField()
```

name = Char field 

tax_code = enum

price = Float 



## Class

class `Bill` have `name`, `tax_code`, and `amount`properties and method:`refundable()`, `tax()`, `amount()`

