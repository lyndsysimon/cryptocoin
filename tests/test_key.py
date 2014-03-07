from nose.tools import *
import unittest

from cryptocoin.key import BitcoinKey

PASSPHRASE = 'correct horse battery staple'
SECRET_EXPONENT = (
    'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a'
)
PRIVATE_KEY = '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS'


class KeyTestCase(unittest.TestCase):

    __test__ = False

    def test_secret_exponent(self):
        with assert_raises(AttributeError):
            _ = self.key.secret_exponent

    def test_private_key(self):
        with assert_raises(AttributeError):
            _ = self.key.private_key


@istest
class PassphraseTestCase(KeyTestCase):
    def setUp(self):
        self.key = BitcoinKey(passphrase=PASSPHRASE)

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