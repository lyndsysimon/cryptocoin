from hashlib import sha256

from .vendor import base58


class BitcoinKey(object):

    _b58_private_key = None
    _passphrase = None

    @property
    def passphrase(self):
        if not self._passphrase:
            raise ValueError('Passphrase cannot be calculated.')
        return self._passphrase

    @property
    def private_key(self):
        if not self._b58_private_key:
            self._b58_private_key = base58.check_encode(
                b'\x80' + self._secret_exponent.digest()
            )
        return self._b58_private_key

    @property
    def _secret_exponent(self):
        if self._passphrase:
            return sha256(self._passphrase.encode('utf-8'))

    @property
    def secret_exponent(self):
        return self._secret_exponent.hexdigest()

    def __init__(self, passphrase=None, private_key=None):
        """

        :param passphrase:
        :param private_key: base58check-encoded
        """
        self._passphrase = passphrase
        self._b58_private_key = private_key
