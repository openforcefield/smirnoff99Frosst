"""
Unit and regression test for the smirnoff99Frosst package.
"""

import glob
import os

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
def test_smirnoff99Frosst_entrypoint(offxml_file_name):
    """Test that the openforcefield toolkit can find and parse the files."""
    import os
    assert os.path.exists(offxml_file_name)


@pytest.mark.parametrize('offxml_file_name', find_all_offxml_files())
def test_smirnoff99Frosst_data_is_loadable(offxml_file_name):
    """Test that the openforcefield toolkit can find and parse the files."""
    from openforcefield.typing.engines.smirnoff import ForceField
    ForceField(offxml_file_name)

