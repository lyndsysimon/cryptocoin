from binascii import unhexlify, hexlify
from hashlib import sha256

_alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
_radix = len(_alphabet)


def _normalize_hex(hex_string):
    """Given a hex string, strip leading and trailing characters

    :param hex_string: string of hex characters

    :raises: `ValueError`if non-hex characters remain after processing

    :return str:hex string

    """
    hex_string = hex_string.lower()

    # Strip out "0x"
    if hex_string[:2] == '0x':
        hex_string = hex_string[2:]

    # Longs have an "L" suffix in Python 2.x
    hex_string = hex_string.strip('l')

    if set(hex_string) - set('0123456789abcdef'):
        raise ValueError('"{} is not a valid hex string'.format(hex_string))

    return hex_string


def b58_encode(hex_string):
    """Encode a given hex string.using Bitcoin's base58 scheme.
    """

    val = int(hex_string, 16)
    encoded = []
    while val >= _radix:
        val, mod = divmod(val, _radix)
        encoded.append(_alphabet[mod])
    if val:
        encoded.append(_alphabet[val])

    if hex_string[:2] == b'00':
        encoded.append(_alphabet[0])

    return ''.join(encoded[::-1])


def b58c_encode(payload, version_byte):
    """Encode a given hex string using Bitcoin's base58chack scheme

    :rtype: string
    """
    payload = _normalize_hex(payload)
    extended_payload = version_byte + payload
    #return extended_payload
    checksum = sha256(sha256(unhexlify(extended_payload)).digest()).digest()[:4]
    return b58_encode(
        extended_payload.encode('utf-8') + hexlify(checksum)
    )


def b58_decode(coded_string):
    val = 0
    for place, char in enumerate(coded_string[::-1]):
        val += (_radix ** place) * _alphabet.index(char)

    return hex(val).strip('L')[2:]


def b58c_decode(coded_string, application_byte=None):
    val = b58_decode(coded_string)
    extended_payload = val[:-8]
    checksum = val[-8:]
    if checksum != sha256(sha256(unhexlify(extended_payload)).digest()).hexdigest()[:8]:
        raise ValueError('Checksum validation failed')

    if application_byte is not None:
        if extended_payload[:2].lower() != application_byte.lower():
            raise ValueError('Application byte check failed')

    return extended_payload[2:]