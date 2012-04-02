class UniqHandlerBase(object):
    def check(self, hash):
        raise NotImplementedError

    def cleanup(self):
        raise NotImplementedError
