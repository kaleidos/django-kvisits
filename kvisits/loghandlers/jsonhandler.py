import simplejson
from .loghandler import LogHandler

import datetime

from .. import settings

class JSONLogHandler(LogHandler):
    instance = None       
    logfile = None

    def __new__(cls, *args, **kargs): 
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance

    def __init__(self):
        self.logfile = file(settings.KVISITS_LOG_FILE_PATH, "a")

    def log_object(self, amp, is_new, request, *args):
        data = {
            "datetime": datetime.datetime.now(),
            "object": amp,
            "is_new": is_new,
            "request_headers": request.HEADERS,
            "extra-args": args,
        }
        self.logfile.write(simplejson.dumps(data)+"\n")

    def log_url(self, url, is_new, request, *args):
        data = {
            "datetime": datetime.datetime.now(),
            "url": url,
            "is_new": is_new,
            "request_headers": request.HEADERS,
            "extra-args": args,
        }
        self.logfile.write(simplejson.dumps(data)+"\n")
