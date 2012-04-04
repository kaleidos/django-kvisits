from .uniqhandlerbase import UniqHandlerBase

class NoUniqHandler(UniqHandlerBase):
    def check(self, visit_hash):
        return True

    def cleanup(self):
        pass
