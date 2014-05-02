import hashlib
from binascii import unhexlify

from ecdsa.curves import SECP256k1
from ecdsa.keys import SigningKey

from .base58 import b58c_decode, b58c_encode


def key_factory(coin_name=None,
                pubkey_hash=None,
                privkey_hash=None):
    """Class factory - creates a base class for a specific currency type.

    This is done so that the `Key` class is not tied to any individual fork of
    Bitcoin.

    :param coin_name: The human-readable name of the cryptocoin. Note that this
                      is used to construct the `__name__` attribute of the
                      returned class.
    :param pubkey_hash: The "application byte" or "version byte" used to
                        calculate a P2H address.
    :param: privkey_hash: The "application byte" or "version byte" used to
                          calculate a WIF-encoded private key.

    :returns: A subclass of `Key`
    """
    return type(
        coin_name + 'Key',
        (Key,),
        {
            '_pubkey_hash': pubkey_hash,
            '_privkey_hash': privkey_hash,
        }
    )


class Key(object):

    #######################
    # Required Attributes #
    #######################

    # Used to calculate a P2H (pay to hash)
    _pubkey_hash = None

    # Used to calculate a WIF-encoded private key
    _privkey_hash = None

    #######################
    # Instance Attributes #
    #######################

    _address = None

    @property
    def address(self):
        """P2H - "pay to hash" - address."""

        if not self._address:
            # Hash the public key twice - using SHA256, then RIPEMD-160
            rip = hashlib.new('ripemd160')
            rip.update(hashlib.sha256(unhexlify(self.public_key)).digest())
            # TODO: This hasn't been tested with leading zero bytes in the hash
            self._address = b58c_encode(rip.hexdigest(), self._pubkey_hash)

        return self._address

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
        if self.secret_exponent:
            sec_exp = self.secret_exponent
            if self.__compressed:
                # append parity byte if key is compressed
                sec_exp = sec_exp + '01'
            self._private_key = b58c_encode(
                sec_exp,
                self._privkey_hash,
            )
            return self._private_key

        # can't find or calculate the private key
        raise AttributeError()

    _public_key = None

    @property
    def public_key(self):
        """
        """

        if self._public_key:
            return self._public_key

        point = SigningKey.from_secret_exponent(
            secexp=int(self.secret_exponent, 16),
            curve=SECP256k1,
            hashfunc=hashlib.sha256,
        ).verifying_key.pubkey.point

        x = hex(point.x())[2:].strip('L')
        y = hex(point.y())[2:].strip('L')

        if self.__compressed:
            return ''.join((
                '02' if point.y() % 2 == 0 else '03',
                x
            ))
        else:
            return ''.join(('04', x, y))


    _secret_exponent = None

    @property
    def secret_exponent(self):
        if self._secret_exponent:
            return self._secret_exponent

        if self._passphrase:
            self._secret_exponent = hashlib.sha256(
                self._passphrase.encode('utf-8')
            ).hexdigest()

        elif self._private_key:
            self._secret_exponent = b58c_decode(
                self._private_key,
                self._privkey_hash,
            )
        else:
            raise AttributeError()

        return self._secret_exponent

    def __init__(self,
                 passphrase=None,
                 private_key=None,
                 secret_exponent=None,
                 public_key=None,
                 address=None,
                 compressed=False):
        """"""
        # check that the class has coin-specific attributes set
        if not self._pubkey_hash or not self._privkey_hash:
            raise UnboundLocalError('All required attributes not set')

        self._passphrase = passphrase
        self._private_key = private_key
        self._secret_exponent = secret_exponent
        self._public_key = public_key
        self._address = address
        self.__compressed = compressed