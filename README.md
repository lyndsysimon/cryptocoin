cryptocoin
==========

Python library for performing tasks related to crypto currencies

# Quickstart

To generate a Bitcoin address from a passphrase:

    from cryptocoin import BitcoinKey

    my_key = BitcoinKey(passphrase="correct horse battery staple")

    my_key.address
    # 1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T

    my_key.public_key
    # 0478d430274f8c5ec1321338151e9f27f4c676a008bdf8638d07c0b6be9ab35c71a1518063243acd4dfe96b66e3f2ec8013c8e072cd09b3834a19f81f659cc3455

    my_key.private_key
    # 5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS