#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#    pyars pyARS.
#    Copyright (c) 2018 Be The Match operated by National Marrow Donor Program. All Rights Reserved.
#
#    This library is free software; you can redistribute it and/or modify it
#    under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation; either version 3 of the License, or (at
#    your option) any later version.
#
#    This library is distributed in the hope that it will be useful, but WITHOUT
#    ANY WARRANTY; with out even the implied warranty of MERCHANTABILITY or
#    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
#    License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this library;  if not, write to the Free Software Foundation,
#    Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA.
#
#    > http://www.fsf.org/licensing/licenses/lgpl.html
#    > http://www.opensource.org/licenses/lgpl-license.php
#

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'certifi==2018.1.18',
    'chardet==3.0.4',
    'idna==2.6',
    'mypy==0.560',
    'numpy',
    'pandas',
    'pkginfo==1.4.1',
    'psutil==5.4.3',
    'python-dateutil==2.6.1',
    'pytz==2018.3',
    'requests==2.18.4',
    'requests-toolbelt==0.8.0',
    'six==1.11.0',
    'tqdm==4.19.5',
    'typed-ast==1.1.0',
    'typing==3.6.4',
    'urllib3==1.22',
    'xlrd==1.1.0'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyard',
    version='0.0.9',
    description="ARD reduction for HLA with python",
    long_description=readme + '\n\n' + history,
    author="Michael Halagan",
    author_email='mhalagan@nmdp.org',
    url='https://github.com/nmdp-bioinformatics/pyARD',
    packages=[
        'pyard',
    ],
    package_dir={'pyard':
                 'pyard'},
    install_requires=requirements,
    license="LGPL 3.0",
    zip_safe=False,
    keywords='pyard',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
