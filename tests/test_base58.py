import unittest

from nose.tools import *

from cryptocoin import base58


class TestEnsureHexString(unittest.TestCase):
    hex_string = '1234567890abcdef'

    def test_0x_prefix(self):
        assert_equal(
            self.hex_string,
            base58._normalize_hex ('0x' + self.hex_string),
        )

    def test_long_suffix(self):
        assert_equal(
            self.hex_string,
            base58._normalize_hex(self.hex_string + 'L'),
        )

    def test_upper_case(self):
        assert_equal(
            self.hex_string,
            base58._normalize_hex(self.hex_string.upper()),
        )

    def test_invalid_character(self):
        with assert_raises(ValueError):
            base58._normalize_hex(self.hex_string + 'X')


class TestB58Encode(unittest.TestCase):
    def test_one_place(self):
        assert_equal(
            'z',
            base58.b58_encode('39'),
        )

    def test_two_places(self):
        assert_equal(
            '21',
            base58.b58_encode('3a')
        )


class TestB58Dencode(unittest.TestCase):
    def test_one_place(self):
        assert_equal(
            '39',
            base58.b58_decode('z'),
        )

    def test_two_places(self):
        assert_equal(
            '3a',
            base58.b58_decode('21')
        )


class TestB58CheckEncode(unittest.TestCase):
    def test_known_input(self):
        assert_equal(
            '6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi',
            base58.b58c_encode(
                payload='c4bbcb1fbec99d65bf59d85c8cb62ee2'
                        'db963f0fe106f483d9afa73bd4e39a8a',
                version_byte='B0',
            )
        )


class Test58Decode(unittest.TestCase):
    def test_known_input(self):
        assert_equal(
            'c4bbcb1fbec99d65bf59d85c8cb62ee2db963f0fe106f483d9afa73bd4e39a8a',
            base58.b58c_decode(
                '6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi',
                'B0'
            )
        )

    def test_invalid_checksum(self):
        with assert_raises(ValueError):
            base58.b58c_decode('asdfasdfasdfasfasdfasdfasdf')

    def test_invalid_version_byte(self):
        with assert_raises(ValueError):
            base58.b58c_decode(
                '6vcfLvDpYnHdbVxoQa6Lmo3k9iR5xVjKwwf3dp4XgmQT3QJywYi',
                '00'
            )