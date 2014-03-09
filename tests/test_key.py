from nose.tools import *
import unittest

from cryptocoin import BitcoinKey

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


class KeyTestCase(unittest.TestCase):

    __test__ = False

    def test_passphrase(self):
        with assert_raises(AttributeError):
            _ = self.key.passphrase

    def test_secret_exponent(self):
        with assert_raises(AttributeError):
            _ = self.key.secret_exponent

    def test_private_key(self):
        with assert_raises(AttributeError):
            _ = self.key.private_key

    def test_address(self):
        assert_equal(
            self.key.address,
            ADDRESS,
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            PUBLIC_KEY,
        )


@istest
class PassphraseTestCase(KeyTestCase):
    def setUp(self):
        self.key = BitcoinKey(passphrase=PASSPHRASE)

    def test_passphrase(self):
        assert_equal(
            self.key.passphrase,
            PASSPHRASE,
        )

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            SECRET_EXPONENT,
        )

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            PRIVATE_KEY,
        )


@istest
class PrivateKeyTestCase(KeyTestCase):
    def setUp(self):
        self.key = BitcoinKey(
            private_key=PRIVATE_KEY)

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            PRIVATE_KEY,
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            PUBLIC_KEY,
        )

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            SECRET_EXPONENT,
        )


@istest
class SecretExponentTestCase(KeyTestCase):
    def setUp(self):
        self.key = BitcoinKey(
            secret_exponent=SECRET_EXPONENT
        )

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            SECRET_EXPONENT,
        )

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            PRIVATE_KEY,
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            PUBLIC_KEY,
        )