# -*- coding: utf-8 -*-
from kvisits import settings
from kvisits.models import UrlVisit

class KVisitsMiddleware(object):
    """ Middleware for count uri visits. """

    def process_request(self, request):
        if settings.KVISITS_URI_WITH_GET_PARAMS:
            print request.get_full_path()
            UrlVisit.objects.add_visit(request, request.get_full_path())
        else:
            UrlVisit.objects.add_visit(request, request.path_info)
