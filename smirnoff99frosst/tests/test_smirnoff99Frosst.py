"""
Unit and regression test for the smirnoff99Frosst package.
"""

import glob
import os

from openforcefield.typing.engines.smirnoff import ForceField
import pytest

from smirnoff99Frosst import get_forcefield_dirs_paths


def find_all_offxml_files():
    """Return a list of the offxml files shipped with the package."""
    file_names = []
    for dir_path in get_forcefield_dirs_paths():
        file_pattern = os.path.join(dir_path, '*.offxml')
        file_paths = [file_path for file_path in glob.glob(file_pattern)]
        file_names.extend([os.path.basename(file_path) for file_path in file_paths])
    return file_names


@pytest.mark.parametrize('offxml_file_name', find_all_offxml_files())
def test_smirnoff99Frosst_installation(offxml_file_name):
    """Test that the openforcefield toolkit can find and parse the files."""
    ForceField(offxml_file_name)
