from nose.tools import *
import unittest

from cryptocoin import BitcoinKey


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
            self.ADDRESS,
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            self.PUBLIC_KEY,
        )


class GenericPassphraseTestCase(KeyTestCase):
    def setUp(self):
        self.key = self.Key(passphrase=self.PASSPHRASE)

    def test_passphrase(self):
        assert_equal(
            self.key.passphrase,
            self.PASSPHRASE,
        )

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            self.SECRET_EXPONENT,
        )

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            self.PRIVATE_KEY,
        )


class GenericPrivateKeyTestCase(KeyTestCase):
    def setUp(self):
        self.key = self.Key(private_key=self.PRIVATE_KEY)

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            self.PRIVATE_KEY,
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            self.PUBLIC_KEY,
        )

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            self.SECRET_EXPONENT,
        )


class GenericSecretExponentTestCase(KeyTestCase):
    def setUp(self):
        self.key = self.Key(secret_exponent=self.SECRET_EXPONENT)

    def test_secret_exponent(self):
        assert_equal(
            self.key.secret_exponent,
            self.SECRET_EXPONENT,
        )

    def test_private_key(self):
        assert_equal(
            self.key.private_key,
            self.PRIVATE_KEY,
        )

    def test_public_key(self):
        assert_equal(
            self.key.public_key,
            self.PUBLIC_KEY,
        )


class GenericPublicKeyTestCase(KeyTestCase):
    def setUp(self):
        self.key = self.Key(public_key=self.PUBLIC_KEY)


class GenericAddressTestCase(KeyTestCase):
    def setUp(self):
        self.key = self.Key(address=self.ADDRESS)

    def test_public_key(self):
        with assert_raises(AttributeError):
            _ = self.key.public_key