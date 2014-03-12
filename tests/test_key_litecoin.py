from nose.tools import istest

from cryptocoin import LitecoinKey
from .test_key import (
    GenericPassphraseTestCase,
    GenericPrivateKeyTestCase,
    GenericSecretExponentTestCase,
    KeyTestCase,
)


class LitecoinKeyTestCase(KeyTestCase):
    __test__ = False

    Key = LitecoinKey

    PASSPHRASE = 'correct horse battery staple'
    SECRET_EXPONENT = (
        'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a'
    )
    PRIVATE_KEY = '6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi'
    PUBLIC_KEY = (
        '04'  # First byte, per the Bitcoin specification
        '78d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71'  # x
        'a1518063243acd4dfe96b66e3f2ec8013c8e072cd09b3834a19f81f659cc3455'  # y
    )
    ADDRESS = 'LdAPi7uXrLLmeh7u57pzkZc3KovxEDYRJq'


@istest
class PassphraseTestCase(GenericPassphraseTestCase, LitecoinKeyTestCase):
    pass


@istest
class PrivateKeyTestCase(GenericPrivateKeyTestCase, LitecoinKeyTestCase):
    pass


@istest
class SecretExponentTestCase(GenericPrivateKeyTestCase, LitecoinKeyTestCase):
    pass