cryptocoin
==========

Cryptocurrencies for Humans.

.. image:: https://api.travis-ci.org/lyndsysimon/cryptocoin.png
   :target: https://travis-ci.org/lyndsysimon/cryptocoin

# Quickstart

To generate a Bitcoin address from a passphrase::

    from cryptocoin import BitcoinKey

    my_key = BitcoinKey(passphrase="correct horse battery staple")

    my_key.address
    # 1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T
