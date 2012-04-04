from ..uniqhandlerbase import UniqHandlerBase
from .models import DBUniqHandlerHashes
from ... import settings
import datetime

class DBUniqHandler(UniqHandlerBase):
    def check(self, visit_hash):
        try:
            hash_obj = DBUniqHandlerHashes.objects.get(visit_hash=visit_hash)
            min_time = datetime.timedelta(seconds=settings.KVISITS_MIN_TIME_BETWEEN_VISITS)
            if (datetime.datetime.now()-min_time) > hash_obj.last_counted_visit:
                hash_obj.last_counted_visit = datetime.datetime.now()
                hash_obj.save()
                return True
            else:
                return False
        except DBUniqHandlerHashes.DoesNotExist:
            DBUniqHandlerHashes(visit_hash, datetime.datetime.now()).save()
            return True

    def cleanup(self):
        min_time = datetime.timedelta(seconds=settings.KVISITS_MIN_TIME_BETWEEN_VISITS)
        DBUniqHandlerHashes.objects.filter(last_counted_visit__lt=datetime.datetime.now()-min_time).delete()
