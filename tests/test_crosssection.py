import pymcabc
import os


def test_xsec_st():
    pymcabc.DefineProcess("A B > A B", mA=4, mB=10, mC=1, pi=15)
    sigma, error = pymcabc.CrossSection().calc_xsection()
    assert sigma < 9e-11, "Sigma over estimated"
    assert sigma > 9e-13, "Sigma over estimated"

def test_xsec_tu():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, pi=15)
    sigma, error = pymcabc.CrossSection().calc_xsection()
    assert sigma < 4e-13, "Sigma over estimated"
    assert sigma > 1e-14, "Sigma over estimated"


