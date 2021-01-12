"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys

import numpy as np


def test_calculate_distance():
    """Test that the calculate distance function calculates what we expect."""
    r1 = np.array([1, 0, 0])
    r2 = np.array([1, 3, 4])

    expected_distance = 5

    observed_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == observed_distance


def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules
