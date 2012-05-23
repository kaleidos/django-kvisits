from django.conf import settings

# The minimum time between two counted visits (in minutes)
KVISITS_MIN_TIME_BETWEEN_VISITS = getattr(settings, 'KVISITS_MIN_TIME_BETWEEN_VISITS', 24 * 60)
KVISITS_IGNORE_URLS = getattr(settings, 'KVISITS_IGNORE_URLS', [])
KVISITS_IGNORE_USER_AGENTS = getattr(
        settings,
        'KVISITS_IGNORE_USER_AGENTS',
        [
                "Teoma.*", "alexa.*", "froogle.*", "Gigabot.*", "inktomi.*",
                "looksmart.*", "URL_Spider_SQL.*", "Firefly",
                "NationalDirectory.*", "Ask Jeeves.*", "TECNOSEEK.*",
                "InfoSeek.*", "WebFindBot.*", "girafabot.*", "crawler.*",
                "www.galaxy.com.*", "Googlebot.*", "Googlebot/2.1.*",
                "Google.*", "Webmaster.*", "Scooter.*", "James Bond.*",
                "Slurp.*", "msnbot.*", "appie.*", "FAST.*", "WebBug.*",
                "Spade.*", "ZyBorg.*", "rabaz.*", "Baiduspider.*",
                "Feedfetcher-Google.*", "TechnoratiSnoop.*", "Rankivabot.*",
                "Mediapartners-Google.*", "Sogou web spider.*",
                "WebAlta Crawler.*", "MJ12bot.*", "Yandex/.*", "YaDirectBot.*",
                "StackRambler.*", "DotBot.*", "dotbot.*"
        ]
)

KVISITS_REQUEST_FIELDS_FOR_HASH = getattr(settings, 'KVISITS_REQUEST_FIELDS_FOR_HASH', ['REMOTE_ADDR', 'HTTP_USER_AGENT'])
KVISITS_URI_WITH_GET_PARAMS = getattr(settings, 'KVISITS_URI_WITH_GET_PARAMS', False)
KVISITS_LOG_ENABLED = getattr(settings, 'KVISITS_LOG_ENABLED', False)
KVISITS_HASH_HANDLER = getattr(settings, 'KVISITS_HASH_HANDLER', 'kvisits.hashhandlers.headershandler.HeadersHandler')
KVISITS_UNIQ_HANDLER = getattr(settings, 'KVISITS_UNIQ_HANDLER', 'kvisits.uniqhandlers.dbuniqhandler.DBUniqHandler')
KVISITS_LOG_HANDLERS = getattr(settings, 'KVISITS_LOG_HANDLERS', ['kvisits.loghandlers.nologhandler.NoLogHandler'])
KVISITS_IGNORE_HANDLERS = getattr(settings, 'KVISITS_IGNORE_HANDLERS', ['kvisits.ignorehandlers.urlignorehandler.UrlIgnoreHandler', 'kvisits.ignorehandlers.useragentignorehandler.UserAgentIgnoreHandler',])
KVISITS_COUNTER_HANDLER = getattr(settings, 'KVISITS_COUNTER_HANDLER', 'kvisits.counterhandlers.dbcounterhandler.DBCounterHandler')
