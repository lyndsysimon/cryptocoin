from .key import key_factory

BitcoinKey = key_factory('Bitcoin', pubkey_hash='00', privkey_hash='80')

__version__ = '0.0.0.dev0'