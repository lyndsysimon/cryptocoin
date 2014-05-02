from .key import key_factory

BitcoinKey = key_factory('Bitcoin', pubkey_hash='00', privkey_hash='80')
LitecoinKey = key_factory('Litecoin', pubkey_hash='30', privkey_hash='B0')

__version__ = '0.0.1'