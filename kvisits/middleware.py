# -*- coding: utf-8 -*-
from kvisits import settings
from kvisits.core import add_url_visit

class KVisitsMiddleware(object):
    """ Middleware for count uri visits. """

    def process_request(self, request):
        '''Count visits to uris auntomatically'''
        if settings.KVISITS_URI_WITH_GET_PARAMS:
            add_url_visit(request, request.get_full_path())
        else:
            add_url_visit(request, request.path_info)
