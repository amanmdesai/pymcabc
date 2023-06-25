import pymcabc
import os

def test_xsec():
    pymcabc.DefineProcess('A A > B B',mA=4,mB=10,mC=1,Ecm=30)
    sigma, error = pymcabc.CrossSection().calc_xsection()
    assert sigma >= 10e-14, \
        "Sigma under estimated"
    assert sigma <= 10e-12, \
        "Sigma over estimated"
