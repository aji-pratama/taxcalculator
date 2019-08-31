from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, csrf_exempt, ALL

from taxcalculator import models as taxcalculator_models


class BillResources(ModelResource):

    class Meta:
        allowed_methods = ['get', 'post']
        fields = ['id', 'name', 'tax_code', 'price']
        authorization = Authorization()
        filtering = {
            'id': ALL
        }
        queryset =  taxcalculator_models.Bill.objects.all()
        resource_name = 'tax'

    def wrap_view(self, view):
        @csrf_exempt
        def wrapper(request, *args, **kwargs):
            request.format = kwargs.pop('format', None)
            wrapped_view = super(BillResources, self).wrap_view(view)
            return wrapped_view(request, *args, **kwargs)
        return wrapper

    def dehydrate(self, bundle):
        bundle.data['tax_type'] = bundle.obj.tax_type()
        bundle.data['refundable'] = bundle.obj.refundable()
        bundle.data['tax'] = bundle.obj.tax()
        bundle.data['amount'] = bundle.obj.amount()
        return bundle
