from django.contrib import admin
from django.urls import path, include

from tastypie.api import Api

from taxcalculator import api as taxcalculator_api

v1_api = Api(api_name='v1')
v1_api.register(taxcalculator_api.BillResources())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1_api.urls)),
]
