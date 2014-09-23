from nose.tools import *
import unittest

from cryptocoin import BitcoinKey
from cryptocoin.wallet import Wallet


class WalletTestCase(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()
        self.keys = [
            BitcoinKey(passphrase='correct horse battery staple')
        ]

    def test_no_keys(self):
        assert_equal(
            0,
            len(self.wallet.keys)
        )

    def test_with_keys(self):
        self.wallet.keys.append(self.keys[0])

        assert_equal(
            [self.keys[0].address],
            list(self.wallet.addresses),
        )
        assert_in(
            self.keys[0].address,
            self.wallet.addresses,
        )