from django.views.generic import View
from django.http import HttpResponse
from .models import TestModel

def view_test_object(request, id):
    test_obj = TestModel.objects.get(pk=id)
    test_obj.add_visit(request)
    return HttpResponse("OK")
