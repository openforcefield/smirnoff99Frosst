"""
Unit and regression test for the smirnoff99Frosst package.
"""

from openforcefield.typing.engines.smirnoff import ForceField
import pytest


pytest.mark.parametrize('offxml_file_name', [
    'smirnoff99Frosst-1.0.0.offxml',
    'smirnoff99Frosst-1.0.1.offxml',
    'smirnoff99Frosst-1.0.2.offxml',
    'smirnoff99Frosst-1.0.3.offxml',
    'smirnoff99Frosst-1.0.4.offxml',
    'smirnoff99Frosst-1.0.5.offxml',
    'smirnoff99Frosst-1.0.6.offxml',
    'smirnoff99Frosst-1.0.7.offxml',
    'smirnoff99Frosst-1.0.8.offxml',
    'smirnoff99Frosst-1.0.9.offxml',
    'smirnoff99Frosst-1.1.8.offxml',
    'smirnoff99Frosst-1.1.9.offxml',
])
def test_smirnoff99Frosst_installation(offxml_file_name):
    """Test that the openforcefield toolkit can find and parse the files."""
    ForceField(offxml_file_name)
