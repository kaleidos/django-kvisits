from kvisits import settings
from django.utils.importlib import import_module

module_name = ".".join(settings.KVISITS_IGNORE_HANDLER.split(".")[0:-1])
class_name = settings.KVISITS_IGNORE_HANDLER.split(".")[-1]
ignorehandler = getattr(import_module(module_name), class_name)()
