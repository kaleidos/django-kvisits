class NoUniqHandler(object):
    def check(self, hash):
        return True

    def cleanup(self):
        pass
