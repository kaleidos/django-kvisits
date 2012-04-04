from django.views.generic import View
from django.http import HttpResponse
from .models import TestModel
from kvisits.core import add_obj_visit

def view_test_object(request, id):
    test_obj = TestModel.objects.get(pk=id)
    add_obj_visit(request, test_obj)
    return HttpResponse("OK")
