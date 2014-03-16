from nose.tools import istest

from cryptocoin import BitcoinKey
from .test_key import (
    GenericAddressTestCase,
    GenericPassphraseTestCase,
    GenericPrivateKeyTestCase,
    GenericPublicKeyTestCase,
    GenericSecretExponentTestCase,
    KeyTestCase,
)


class BitcoinKeyTestCase(KeyTestCase):
    __test__ = False

    Key = BitcoinKey

    PASSPHRASE = 'correct horse battery staple'
    SECRET_EXPONENT = (
        'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a'
    )
    PRIVATE_KEY = '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS'
    PUBLIC_KEY = (
        '04'  # First byte, per the Bitcoin specification
        '78d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71'  # x
        'a1518063243acd4dfe96b66e3f2ec8013c8e072cd09b3834a19f81f659cc3455'  # y
    )
    ADDRESS = '1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T'


@istest
class PassphraseTestCase(GenericPassphraseTestCase, BitcoinKeyTestCase):
    pass


@istest
class PrivateKeyTestCase(GenericPrivateKeyTestCase, BitcoinKeyTestCase):
    pass


@istest
class SecretExponentTestCase(GenericSecretExponentTestCase, BitcoinKeyTestCase):
    pass


@istest
class PublicKeyTestCase(GenericPublicKeyTestCase, BitcoinKeyTestCase):
    pass


@istest
class AddressTestCase(GenericAddressTestCase, BitcoinKeyTestCase):
    pass