import hashlib

class HashHandlerBase(object):
    def gen_hash(self, request, **kwargs):
        raise NotImplementedError


class Sha1HashHandler(HashHandlerBase):
    def gen_hash(self, request, **kwargs):
        items = self.get_hash_items(request, **kwargs)
        h = hashlib.sha1()
        for item in items:
            h.update(item)
        return h.hexdigest()

    def get_hash_items(self, request, **kwargs):
        raise NotImplementedError
