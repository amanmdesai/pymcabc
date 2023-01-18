import pymcabc
import os

# test if the file is prepared
def test_eventGen():
    pymcabc.DefineProcess('A A > B B',mA=4,mB=10,mC=1,Ecm=30)
    pymcabc.CrossSection().calc_xsection()
    pymcabc.PlotData.file('name.root')
    assert 'name.root' in os.listdir(), \
        "file not created"

def test_xsec():
    pymcabc.DefineProcess('A A > B B',mA=4,mB=10,mC=1,Ecm=30)
    sigma, error = pymcabc.CrossSection().calc_xsection()
    assert sigma <= 10e-14, \
        "Sigma under estimated"
    assert sigma >= 10e-12, \
        "Sigma over estimated"
