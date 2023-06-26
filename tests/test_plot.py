import pymcabc
import os


# test if the file is prepared
def test_plot():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, Ecm=30)
    pymcabc.CrossSection().calc_xsection()
    pymcabc.SaveEvent(100, boolDecay=True, boolDetector=True).to_root(
        "test_eventGen_detector_decay.root"
    )
    pymcabc.PlotData.file("test_eventGen_detector_decay.root")
    assert "B_E_decay_A.png" in os.listdir(), "file not created"
