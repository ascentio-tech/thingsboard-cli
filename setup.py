# Copyright (c) 2019 Ascentio Technologies S.A. All rights reserved.
#
# This program is confidential and proprietary to Ascentio Technologies S.A.,
# and may not be copied, reproduced, modified, disclosed to
# others, published or used, in whole or in part, without the
# express prior written permission of Ascentio Technologies S.A.

__copyright__ = 'Copyright (c) 2019 Ascentio Technologies S.A.'


import os
import sys
from setuptools import (setup, find_packages, )


NAME = "thingsboard-cli"

SCRIPT = [os.path.join('bin', NAME)]

DESCRIPTION = "Thingsboard util CLI"

here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open('thingsboard_cli/version.py') as fp:
    exec(fp.read(), version)

setup(
    name=NAME,
    version=version['__version__'],
    url='',
    license='',
    author="ASC",
    keywords="",
    setup_requires=["pytest-runner", "flake8"] if 'test' in sys.argv else [],
    tests_require=['pytest==3.0.7', 'pytest-quickcheck==0.8.2',
                   'coverage==4.3.4', 'pytest-cov==2.4.0',
                   'mock==1.3.0', 'testfixtures==4.9.1'],
    install_requires=['click',
                      'requests',
                      'thingsboard-client>=2.3.0'
                      ],
    author_email="gmatheu@ascentio.com.ar",
    description=DESCRIPTION,
    long_description='Thingsboard util CLI',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points='''
        [console_scripts]
        thingsboard_cli=thingsboard_cli.cli:main
    ''',
)
