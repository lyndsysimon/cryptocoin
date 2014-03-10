from binascii import unhexlify, hexlify
from hashlib import sha256

_alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
_radix = len(_alphabet)


def b58_encode(hex_string):
    val = int(hex_string, 16)
    encoded = []
    while val >= _radix:
        val, mod = divmod(val, _radix)
        encoded.append(_alphabet[mod])
    if val:
        encoded.append(_alphabet[val])

    return ''.join(encoded[::-1])


def b58c_encode(payload, application_byte):
    """ Encode a given hex string using Bitcoin's base58 scheme, with a checksum

    :rtype: string
    """
    extended_payload = application_byte + payload
    #return extended_payload
    checksum = sha256(sha256(unhexlify(extended_payload)).digest()).digest()[:4]
    return b58_encode(extended_payload.encode('utf-8') + hexlify(checksum))


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
        if extended_payload[:2] != application_byte:
            raise ValueError('Application byte check failed')

    return extended_payload[2:]