import pymcabc
import os


def test_xsec_st():
    pymcabc.DefineProcess("A B > A B", mA=4, mB=10, mC=1, pi=15)
    sigma, error = pymcabc.CrossSection().calc_xsection()
    print(sigma)
    assert sigma > 7e-13, "Sigma under estimated"
    assert sigma < 1e-11, "Sigma over estimated"


def test_xsec_tu():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, pi=15)
    sigma, error = pymcabc.CrossSection().calc_xsection()
    assert sigma > 1e-13, "Sigma under estimated"
    assert sigma < 7e-11, "Sigma over estimated"
