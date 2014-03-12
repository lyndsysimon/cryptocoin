cryptocoin
==========

Python library for performing tasks related to crypto currencies

# Quickstart

To generate a Bitcoin address from a passphrase::

    from cryptocoin import BitcoinKey

    my_key = BitcoinKey(passphrase="correct horse battery staple")

    my_key.address
    # 1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T