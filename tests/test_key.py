from nose.tools import *
import unittest

from cryptocoin.key import BitcoinKey


class PassphraseTestCase(unittest.TestCase):
    def setUp(self):
        self.key = BitcoinKey(passphrase='correct horse battery staple')

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a',
        )

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        )


class PrivateKeyTestCase(unittest.TestCase):
    def setUp(self):
        self.key = BitcoinKey(
            private_key='5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS')

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
        )