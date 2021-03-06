#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

from glob import glob
from os.path import basename, dirname, join, splitext
import io
import re

from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8'),
    ) as fh:
        return fh.read()


setup(
    name='oemof.db',
    # Unfortunately we can't use a `__version__` attribute on `oemof.db` as
    # we can't import that module here. It depends on packages which might
    # not be available prior to installation.
    version='0.0.6',
    license='MIT',
    description=(
        'Open Energy Modelling Framework'
        ' - An extension for all database related things'
    ),
    long_description='%s\n%s'
    % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub(
            '', read('README.rst')
        ),
        '\n'.join(
            [
                re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read(path))
                for path in glob('docs/whatsnew/*')
            ]
        ),
    ),
    author='oemof developer group',
    author_email='oemof@rl-institut.de',
    url='https://github.com/oemof/oemof.db',
    packages=['oemof'] + ['oemof.' + p for p in find_packages('src/oemof')],
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        #   http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://oemofdb.readthedocs.io/',
        'Changelog': 'https://oemofdb.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/oemof/oemof.db/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
        'oemof',
        'sqlalchemy >= 1.0',
        'keyring >= 4.0',
        'shapely',
        'psycopg2',
        'keyrings.alt',
        'pandas >=0.19.1',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
)
