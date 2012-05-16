from kvisits import settings
from django.utils.importlib import import_module

__all__ = ('hashhandler',)

module_name = ".".join(settings.KVISITS_HASH_HANDLER.split(".")[0:-1])
class_name = settings.KVISITS_HASH_HANDLER.split(".")[-1]
hashhandler = getattr(import_module(module_name), class_name)()

