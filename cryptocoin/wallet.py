class Wallet(object):
    def __init__(self):
        self.keys = []

    @property
    def addresses(self):
        return (key.address for key in self.keys)