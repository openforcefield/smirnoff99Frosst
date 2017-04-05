"""
Setup script to install the smirnoff99Frosst.ffxml as a python package
"""

import sys,os
from os.path import relpath, join

from setuptools import setup, find_packages

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

descr = """
This provides the first general-purpose implementation of a SMIRKS Native Open Force Field (SMIRNOFF) as implemented by SMARTY and its ForceField class (in smarty.forcefield) for parameterizing small molecules for OpenMM.
"""

setup(
    name                 = 'smirnoff99frosst',
    version              = '1.0.5',
    description          = 'SMIRNOFF Forcefield parameters',
    long_description     = descr,
    url                  = 'https://github.com/open-forcefield-group/smirnoff99Frosst',
    author               = 'Christopher I. Bayly, Caitlin C. Bannan, David L. Mobley',
    author_email         = 'dmobley@uci.edu',
    license              = 'MIT',
    platforms            = ['Linux-64', 'Mac OSX-64', 'Unix-64'],
    packages             = find_packages()+['smirnoff99frosst'],
    include_package_data = True
)
