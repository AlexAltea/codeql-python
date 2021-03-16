#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
import setuptools

CODEQL_VERSION = '2.4.5'
CODEQL_REPOSITORY_URL = 'https://github.com/AlexAltea/codeql-python'
CODEQL_DOWNLOAD_URL = 'https://github.com/AlexAltea/codeql-python/tarball/' + CODEQL_VERSION

# Description
CODEQL_DESCRIPTION = """CodeQL for Python
=================

Unofficial Python 3.x bindings for the CodeQL CLI application.

More information at: https://github.com/AlexAltea/codeql-python
"""

setuptools.setup(
    name='codeql-python',
    version=CODEQL_VERSION,
    description='Unofficial Python bindings for CodeQL CLI',
    long_description=CODEQL_DESCRIPTION,
    license='MIT',
    author='Alexandro Sanchez Bach',
    author_email='alexandro@phi.nz',
    url=CODEQL_REPOSITORY_URL,
    download_url=CODEQL_DOWNLOAD_URL,
    packages=['codeql-python'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
    ],
)
