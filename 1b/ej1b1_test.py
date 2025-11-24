import pytest
from ej1b1 import mcd, mcd_list, mcm, mcm_list

def test_mcd():
    assert mcd(54, 24) == 6, "The MCD of 54 and 24 should be 6."

def test_mcd_list():
    assert mcd_list([8, 12, 16]) == 4, "The MCD of [8, 12, 16] should be 4."

def test_mcm():
    assert mcm(4, 6) == 12, "The MCM of 4 and 6 should be 12."

def test_mcm_list():
    assert mcm_list([4, 6, 8]) == 24, "The MCM of [4, 6, 8] should be 24."
