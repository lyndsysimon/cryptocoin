from setuptools import setup
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='cryptocoin',
    version=find_version('cryptocoin', '__init__.py'),
    description="Cryptocurrencies for Humans",
    long_description=long_description,

    url='http://github.com/lyndsysimon/cryptocoin',

    license='Apache',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: Apache Software License',
    ],

    keywords='bitcoin cryptocurrency',

    packages=['cryptocoin'],

    install_requires=['ecdsa', ],
)
