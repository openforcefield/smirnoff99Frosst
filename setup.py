"""
Setup script to install the smirff99Frosst.ffxml as a python package
"""

import sys,os
from os.path import relpath, join

from setuptools import setup, find_packages

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

descr = """
This provides the first general-purpose implementation of a Smirks Force Field (SMIRFF) as implemented by SMARTY and its ForceField class (in smarty.forcefield) for parameterizing small molecules for OpenMM.
"""

setup(
    name                 = 'smirff99frosst',
    version              = '1.0.3',
    description          = 'SMIRNOFF Forcefield parameters',
    long_description     = descr,
    url                  = 'https://github.com/open-forcefield-group/smirff99Frosst',
    author               = 'Christopher I. Bayly, Caitlin C. Bannan, David L. Mobley',
    author_email         = 'dmobley@uci.edu',
    license              = 'MIT',
    platforms            = ['Linux-64', 'Mac OSX-64', 'Unix-64'],
    packages             = find_packages()+['smirff99frosst'],
    include_package_data = True,
    zip_safe             = False
)
