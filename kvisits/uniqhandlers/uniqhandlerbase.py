class UniqHandlerBase(object):
    def check(self, visit_hash):
        raise NotImplementedError

    def cleanup(self):
        raise NotImplementedError
