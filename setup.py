#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '7.2.2.1'

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-anysearch-dsl',
    version=version,
    description="""Wrapper around elasticsearch-dsl and opensearch-dsl for Django models""",
    long_description=readme + '\n\n' + history,
    author='Sabricot',
    maintainer='Artur Barseghyan',
    url='https://github.com/django-anysearch/django-anysearch-dsl',
    packages=[
        'django_elasticsearch_dsl',
    ],
    include_package_data=True,
    install_requires=[
        'six',
        'anysearch>=0.2.2',
    ],
    extras_require={
        "elasticsearch": [
            "elasticsearch",
            "elasticsearch-dsl",
            # "elasticsearch-dsl>=7.2.0<8.0.0",
        ],
        "opensearch": [
            "opensearch-py",
            "opensearch-dsl",
        ],
    },
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='django elasticsearch elasticsearch-dsl',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
