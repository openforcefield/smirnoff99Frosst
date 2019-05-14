"""
SMIRNOFF99Frosst
A general small molecule forcefield descended from AMBER99 and parm@Frosst in the SMIRNOFF format.
"""

# Add imports here
from .smirnoff99frosst import get_forcefield_dir_paths

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
