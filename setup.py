"""
Setup script to install the smirnoff99Frosst.ffxml as a python package
"""

import sys,os
from os.path import relpath, join
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_package_data(data_root, package_root):
    files = []
    for root, dirnames, filenames in os.walk(data_root):
        for fn in filenames:
            files.append(relpath(join(root, fn), package_root))
    return files

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

descr = """
This provides the first general-purpose implementation of a SMIRKS Native Open Force Field (SMIRNOFF) as implemented by SMARTY and its ForceField class (in smarty.forcefield) for parameterizing small molecules for OpenMM. (Note that the forcefield class is being migrated to openforcefield rather than smarty.)
"""

setup(
    name                 = 'smirnoff99frosst',
    version              = '1.0.6',
    description          = 'SMIRNOFF Forcefield parameters',
    long_description     = descr,
    url                  = 'https://github.com/open-forcefield-group/smirnoff99Frosst',
    author               = 'Christopher I. Bayly, Caitlin C. Bannan, David L. Mobley',
    author_email         = 'dmobley@uci.edu',
    license              = 'MIT',
    platforms            = ['Linux-64', 'Mac OSX-64', 'Unix-64'],
    packages             = find_packages()+['smirnoff99frosst'],
    package_data = {'smirnoff99frosst':find_package_data('smirnoff99frosst/', 'smirnoff99frosst')},
    include_package_data = True
)
