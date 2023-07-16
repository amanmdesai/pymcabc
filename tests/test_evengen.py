import pymcabc
import os
import pytest


# test if the file is prepared
def test_eventGen_detector_decay():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, pi=30)
    pymcabc.CrossSection().calc_xsection()
    pymcabc.SaveEvent(100, boolDecay=True, boolDetector=True).to_root(
        "test_eventGen_detector_decay.root"
    )
    # pymcabc.PlotData.file('test_eventGen_detector_decay.root')
    assert "test_eventGen_detector_decay.root" in os.listdir(), "file not created"


def test_eventGen_decay():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, pi=30)
    pymcabc.CrossSection().calc_xsection()
    pymcabc.SaveEvent(100, boolDecay=True, boolDetector=False).to_root(
        "test_eventGen_decay.root"
    )
    assert "test_eventGen_decay.root" in os.listdir(), "file not created"


def test_eventGen_detector():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, pi=30)
    pymcabc.CrossSection().calc_xsection()
    pymcabc.SaveEvent(100, boolDecay=False, boolDetector=True).to_root(
        "test_eventGen_detector.root"
    )
    assert "test_eventGen_detector.root" in os.listdir(), "file not created"


def test_eventGen():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, pi=30)
    pymcabc.CrossSection().calc_xsection()
    pymcabc.SaveEvent(100, boolDecay=False, boolDetector=False).to_root(
        "test_eventGen.root"
    )
    assert "test_eventGen.root" in os.listdir(), "file not created"


def test_csv_output_reject():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, pi=30)
    pymcabc.CrossSection().calc_xsection()
    with pytest.raises(
        Exception, match="Output supported with .root extension only"):
        pymcabc.SaveEvent(100, boolDecay=False, boolDetector=False).to_root("test_eventGen.csv")

