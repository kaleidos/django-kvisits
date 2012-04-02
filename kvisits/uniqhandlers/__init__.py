from kvisits import settings
from django.utils.importlib import import_module

__all__ = ('uniqhandler',)

module_name = ".".join(settings.KVISITS_UNIQ_HANDLER.split(".")[0:-1])
class_name = settings.KVISITS_UNIQ_HANDLER.split(".")[-1]
uniqhandler = getattr(import_module(module_name), class_name)()
