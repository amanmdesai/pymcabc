import pymcabc
import os
import json
import pytest


def test_identify_tu():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, pi=30)
    with open("library.json", "r") as f:
        library = json.load(f)
    assert library["m1"][0] == 4
    assert library["m2"][0] == 4
    assert library["m3"][0] == 10
    assert library["m4"][0] == 10
    assert library["mx"][0] == 1
    assert library["pi"][0] == 30
    library["process_type"][0] == "tu"


def test_identify_st():
    pymcabc.DefineProcess("A B > A B", mA=4, mB=10, mC=1, pi=30)
    with open("library.json", "r") as f:
        library = json.load(f)
    assert library["m1"][0] == 4
    assert library["m2"][0] == 10
    assert library["m3"][0] == 4
    assert library["m4"][0] == 10
    assert library["mx"][0] == 1
    assert library["pi"][0] == 30
    library["process_type"][0] == "st"


def test_negative_param():
    with pytest.raises(Exception, match="Negative masses not accepted"):
        pymcabc.DefineProcess("A B > A B", mA=4, mB=-10, mC=1, pi=30)

def test_negative_param_2():
    with pytest.raises(
        Exception, match="Negative or Zero absolute momentum not accepted"):
        pymcabc.DefineProcess("A B > A B", mA=4, mB=10, mC=1, pi=-30)


"""
def test_feynmandiagram_tu():
    pymcabc.DefineProcess('A A > B B',mA=4,mB=10,mC=1,pi=30)
    pymcabc.FeynmanDiagram()
    assert 'uchan.pdf' in os.listdir(), \
        "file not created"
    assert 'tchan.pdf' in os.listdir(), \
        "file not created"

def test_feynmandiagram_st():
    pymcabc.DefineProcess('A B > A B',mA=4,mB=10,mC=1,pi=30)
    pymcabc.FeynmanDiagram()
    assert 'schan.pdf' in os.listdir(), \
        "file not created"
    assert 'tchan.pdf' in os.listdir(), \
        "file not created"
"""
