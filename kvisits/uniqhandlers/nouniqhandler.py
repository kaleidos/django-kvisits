from .uniqhandlerbase import UniqHandlerBase

class NoUniqHandler(UniqHandlerBase):
    def check(self, hash):
        return True

    def cleanup(self):
        pass
