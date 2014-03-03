'''Library for encoding/decoding Base58check.

Copyright Corgan Labs, used with permission under the MIT license.
https://github.com/jmcorgan/bip32utils/
'''

from hashlib import sha256

__base58_alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__base58_radix = len(__base58_alphabet)


def __string_to_int(data):
    """Convert string of bytes Python integer, MSB

    :return: An ``int`` (or ``long``)"""
    val = 0
    for (i, c) in enumerate(data[::-1]):
        val += (256**i) * c
    return val


def encode(data):
    """Encode string into Bitcoin base58"""
    enc = ''
    val = __string_to_int(data)
    while val >= __base58_radix:
        val, mod = divmod(val, __base58_radix)
        enc = __base58_alphabet[mod] + enc
    if val:
        enc = __base58_alphabet[val] + enc

    # Pad for leading zeroes
    n = len(data)-len(str(data).lstrip('\0'))
    return __base58_alphabet[0]*n + enc


def check_encode(raw):
    """Encode raw string into Bitcoin base58 with checksum"""

    chk = bytearray(sha256(sha256(raw).digest()).digest()[:4])
    return encode(raw+chk)


def decode(data):
    """Given a Bitcoin base58-encoded string, return the data and checksum

    :return: (``str`` data, ``list`` checksum)
    """
    val = 0
    for (i, c) in enumerate(data[::-1]):
        val += __base58_alphabet.find(c) * (__base58_radix**i)
    dec = []
    while val >= 256:
        val, mod = divmod(val, 256)
        dec.append(int(mod))
    if val:
        dec.append(int(val))
    return ''.join([chr(x) for x in dec[::-1][:-4]]), dec[::-1][-4:]


def check_decode(enc):
    """Decode string from Bitcoin base58 and test checksum

    :return: """
    data, provided_check = decode(enc)
    computed_check = sha256(sha256(data.encode('utf-8')).digest()).digest()[:4]

    if isinstance(computed_check[0], bytes):
        computed_check = [int(ord(i)) for i in computed_check]

    if bytes(provided_check) != bytes(computed_check):
        raise ValueError("base58 decoding checksum error")
    else:
        return data


if __name__ == '__main__':
    assert(__base58_radix == 58)
    data = 'now is the time for all good men to come to the aid of their country'
    enc = check_encode(data)
    assert(check_decode(enc) == data)