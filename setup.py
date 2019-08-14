#!/usr/bin/env python
from setuptools import setup

setup(
    name='psycopg2',
    version='2.8.3',
    description='psycopg2',
    author='author_psycopg2',
    maintainer='maintainer_psycopg2',
    maintainer_email='email_maintainer',
    url='https://github.com/philipppahl/awslambda-psycopg2',
    license='Apache',
    packages=['psycopg2'],
    package_data={'psycopg2': ['_psycopg.cpython-37m-x86_64-linux-gnu.so']},
    # long_description=open('README').read(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    # install_requires=['requests'],
)
