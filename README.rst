==========
cryptocoin
==========

Cryptocurrencies for Humans.

========= ========
Service   Status
========= ========
Travis CI |travis|
========= ========

.. |travis| image:: https://api.travis-ci.org/lyndsysimon/cryptocoin.png
   :target: https://travis-ci.org/lyndsysimon/cryptocoin

Cryptocoin is an attempt to create a stable, easy-to-use package that optimizes
for developer happiness. In the same way that `Requests`_ makes working with
HTTP much less painful, Cryptocoin is intended to ease working with
cryptocurrencies.

.. _Requests: https://github.com/kennethreitz/requests

Project Goals
=============

* **Cross-version compatibility**: Currently Python 2.7, 3.3, and PyPy
* **Test Coverage**: 100%!
* **Support for multiple currencies**

Quickstart
==========

To generate a Bitcoin address from a passphrase::

    > from cryptocoin import BitcoinKey
    
    > my_key = BitcoinKey(passphrase="correct horse battery staple")

    > my_key.address
    1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T
