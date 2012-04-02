from kvisits import settings
from django.utils.importlib import import_module

__all__ = ('loghandlers',)

loghandlers = []
for log_handler_conf in settings.KVISITS_LOG_HANDLERS:
    module_name = ".".join(log_handler_conf.split(".")[0:-1])
    class_name = log_handler_conf.split(".")[-1]
    loghandlers.append(getattr(import_module(module_name), class_name)())
