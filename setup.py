#!/usr/bin/env python3.3
# encoding: utf-8

from distutils.core import setup

setup(
    name='maintboot',
    version='0.1.0',
    author='Gabriel de Perthuis',
    author_email='g2p.code+maintboot@gmail.com',
    url='https://github.com/g2p/maintboot',
    license='GNU GPL',
    keywords='kexec maintenance booting',
    description='run commands outside of the current OS',
    scripts=['bin/maintboot'],
    classifiers='''
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.3
        License :: OSI Approved :: GNU General Public License (GPL)
        Operating System :: POSIX :: Linux
        Topic :: Utilities
    '''.strip().splitlines(),
    long_description='''
    maintboot runs commands outside of the current OS,
    with exclusive access to the system and hardware.

    This can be useful to run maintenance tasks,
    like repartitioning, in a controlled environment.

    Maintboot builds an appliance on the fly from a list
    of packages (using supermin).
    It then loads the appliance with kexec, bypassing
    the bios, and runs the maintenance script in that
    new context.

    See `github.com/g2p/maintboot <https://github.com/g2p/maintboot#readme>`_
    for installation and usage instructions.''')

