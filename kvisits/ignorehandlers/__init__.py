from kvisits import settings
from django.utils.importlib import import_module

__all__ = ('ignorehandlers',)

ignorehandlers = []
for ignore_handler_conf in settings.KVISITS_IGNORE_HANDLERS:
    module_name = ".".join(ignore_handler_conf.split(".")[0:-1])
    class_name = ignore_handler_conf.split(".")[-1]
    ignorehandlers.append(getattr(import_module(module_name), class_name)())
