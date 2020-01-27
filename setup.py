#!/usr/bin/env python3

from setuptools import setup, find_packages
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

setup(

    name='PTGC',

    # la version du code
    version='1.0',
    packages=find_packages(),
    author="Delevoye Guillaume",
    author_email="delevoye.guillaume@gmail.com",
    description="Annoying growth calculations for paramecium tetraurelia",
    long_description=open('README.md').read(),
    url='https://github.com/GDelevoye/PTGC.git',

    include_package_data=True,
    entry_points={'console_scripts': ['PTGC_GUI=PTGC.launchers.PTGC_GUI:PTGC_GUI']},

    # La liste des marqueurs autorisés
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.

    classifiers=[
        "Programming Language :: Python",
        "License :: The clear BSD Licence",
        "Natural Language :: French",
        "Operating System :: Ubuntu 18.04 LTS",
        "Programming Language :: Python :: 3.6"
    ],

    license="WTFPL",
)
