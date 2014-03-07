from hashlib import sha256

from .vendor import base58


def key_factory(coin_name=None, application_byte=None):
    return type(
        coin_name + 'Key',
        (Key,),
        {
            '_application_byte': application_byte,
        }
    )


class Key(object):

    # Required attributes
    _application_byte = None


    # instance attributes
    _passphrase = None

    @property
    def passphrase(self):
        """ The plaintext passphrase.

        Note that this is available only if a passphrase was passed upon
        instantiation.

        :raises: ``AttributeError`` if not instantiated with a passphrase.
        :rtype: str
        """
        if self._passphrase:
            return self._passphrase

        #passphrase must be provided; it can't be calculated.
        raise AttributeError()

    _private_key = None

    @property
    def private_key(self):
        """ The private key (WIF/wallet import format)

        see: https://en.bitcoin.it/wiki/Wallet_import_format

        :raises: ``AttributeError`` if secret exponent is not known
        :rtype: str
        """

        # If the private key is available directly, return it
        if self._private_key:
            return self._private_key

        # if the secret exponent exists, generate and cache the private key
        if self._secret_exponent:
            self._private_key = base58.check_encode(
                self._application_byte + self._secret_exponent.digest()
            )
            return self._private_key

        # can't find or calculate the private key
        raise AttributeError()

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
        # check that the class has coin-specific attributes set
        if not self._application_byte:
            raise UnboundLocalError('All required attributes not set')

        self._passphrase = passphrase
        self._private_key = private_key
