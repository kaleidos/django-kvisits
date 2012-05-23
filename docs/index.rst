Welcome to django-kvisits's documentation!
==========================================

django-kvisits allows you to count visits to urls (automatically) or to objects (manually).

Installation
------------

::

    pip install django-kvisits
    

Configuration
-------------

Add ``kvisits``, ``kvisits.counterhandlers.dbcounterhandler``, ``kvisits.uniqhandlers.dbuniqhandler`` and ``django.contrib.sites`` to your ``INSTALLED_APPS``

::

    INSTALLED_APPS = (
        ...
        'django.contrib.sites',
        'kvisits'
        'kvisits.counterhandlers.dbcounterhandler'
        'kvisits.uniqhandlers.dbuniqhandler'
        ...
    )
    
If you want url automatic counting, you have to add the ``kvisits.middleware.KVisitsMiddleware`` to your settings ``MIDDLEWARE_CLASSES``

::

    MIDDLEWARE_CLASSES = (
        ...
        'kvisits.middleware.KVisitsMiddleware',
        ...
    )

Usage
-----

To add a visit to an object make use of :attr:`kvisits.core.add_obj_visit`

::

    from kvisits.core import add_obj_visit

    obj = MyClass.objects.get(pk=1)
    add_obj_visit(request, obj)


To add a visit to an url manullay make use of :attr:`kvisits.core.add_url_visit`

::

    from kvisits.core import add_url_visit

    add_url_visit(request, '/foo/bar/')

Settings
--------

There are a couple of editable settings

.. attribute:: KVISITS_MIN_TIME_BETWEEN_VISITS

    :Default: `24 * 60`
    :type: int
    
    Minimun time (in minutes) between two visits to be counted as diferent visits.
    
.. attribute:: KVISITS_IGNORE_URLS
    
    :Default: `[]`
    :type: list
    
    List of regular expresions to be ignored by the urlignorehandler if is enabled.
        
.. attribute:: KVISITS_IGNORE_USER_AGENTS
    
    :Default: `["Teoma.*", "alexa.*", "froogle.*", "Gigabot.*", "inktomi.*", "looksmart.*", "URL_Spider_SQL.*", "Firefly", "NationalDirectory.*", "Ask Jeeves.*", "TECNOSEEK.*", "InfoSeek.*", "WebFindBot.*", "girafabot.*", "crawler.*", "www.galaxy.com.*", "Googlebot.*", "Googlebot/2.1.*", "Google.*", "Webmaster.*", "Scooter.*", "James Bond.*", "Slurp.*", "msnbot.*", "appie.*", "FAST.*", "WebBug.*", "Spade.*", "ZyBorg.*", "rabaz.*", "Baiduspider.*", "Feedfetcher-Google.*", "TechnoratiSnoop.*", "Rankivabot.*", "Mediapartners-Google.*", "Sogou web spider.*", "WebAlta Crawler.*", "MJ12bot.*", "Yandex/.*", "YaDirectBot.*", "StackRambler.*", "DotBot.*", "dotbot.*"]`
    :type: list
    
    List of regular expresions to be ignored by the useragentignorehandler if is enabled.
    
.. attribute:: KVISITS_REQUEST_FIELDS_FOR_HASH

    :Default: `['REMOTE_ADDR', 'HTTP_USER_AGENT']`
    :type: list
    
    List of headers from request used to generate the visit hash, used by the `HeadersHandler`.
    
.. attribute:: KVISITS_URI_WITH_GET_PARAMS

    :Default: `False`
    :type: boolean
    
    Enable or disable include the GET params in the url visit counting hashes,
    this means thats the same url with diferent get parameters are counted as
    diferent urls.
    
.. attribute:: KVISITS_LOG_ENABLED

    :Default: `False`
    :type: boolean
    
    Enable or disable the execution of the log handlers.
    
.. attribute:: KVISITS_HASH_HANDLER

    :Default: `kvisits.hashhandlers.headershashhandler.HeadersHashHandler`
    :type: class
    
    Define the hash generator handler class.
    
.. attribute:: KVISITS_UNIQ_HANDLER

    :Default: `kvisits.uniqhandlers.dbuniqhandler.DBUniqHandler`
    :type: class
    
    Define the uniq handler class.
    
.. attribute:: KVISITS_LOG_HANDLERS

    :Default: `[kvisits.loghandlers.nologhandler.NoLogHandler]`
    :type: list
    
    Define the log handler classes.
    
.. attribute:: KVISITS_IGNORE_HANDLERS

    :Default: `[kvisits.ignorehandlers.urlignorehandler.UrlIgnoreHandler, kvisits.ignorehandlers.useragentignorehandler.UserAgentIgnoreHandler,]`
    :type: list
    
    Define the ignore handler classes.
    
.. attribute:: KVISITS_COUNTER_HANDLER

    :Default: `kvisits.counterhandlers.dbcounterhandler.DBCounterHandler`
    :type: class
    
    Define the counter handler classes.
    
Advanced usage
--------------

You can modify deeply the behavior of django-kvisits replacing the handlers
classes with your own handlers implementations.

API
---

.. toctree::
    :maxdepth: 3
    
    kvisits

Made by `Kaleidos <http://www.kaleidos.net/>`_. 
