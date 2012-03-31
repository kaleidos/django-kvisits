from kvisits import settings
from django.utils.importlib import import_module

__all__ = ('loghandler')

module_name = ".".join(settings.KVISITS_LOG_HANDLER.split(".")[0:-1])
class_name = settings.KVISITS_LOG_HANDLER.split(".")[-1]
loghandler = getattr(import_module(module_name), class_name)()
