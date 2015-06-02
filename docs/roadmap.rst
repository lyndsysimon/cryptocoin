Roadmap
=======

Data Model
----------

Key
+++

A ``Key`` object is a representation of a single key or address. This can
get a tad murky though, as not all attributes of this object may be derived
from the data provided.

As an example of a minimal amount of data provided, a ``Key`` may be
instantiated with only an address specified. In that case, the user may
want to check the balance of the address, or bundle it into a wallet. If
the user attempted to generate a signed transaction with this object, an
exception should be raised, as you cannot sign a transaction without the
private key used to generate the address.

Wallet
++++++

A ``Wallet`` is a collection of keys. It should expose attributes that are
derived from its component keys - for instance, "balance" - but it should
also expose attributes specific to the wallet itself - for instance,
"generate_key".

Care should be taken to support hierarchical deterministic wallets now or in
the near future, so that a wallet may be instantiated with a seed value and
keys generated through a specific algorithm.
