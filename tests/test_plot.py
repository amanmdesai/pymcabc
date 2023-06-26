import pymcabc
import os


# test if the file is prepared
def test_plot_st():
    pymcabc.DefineProcess("A B > A B", mA=4, mB=10, mC=1, pi=30)
    pymcabc.CrossSection().calc_xsection()
    pymcabc.SaveEvent(100, boolDecay=True, boolDetector=True).to_root(
        "test_eventGen_detector_decay_st.root"
    )
    pymcabc.PlotData.file("test_eventGen_detector_decay_st.root")
    assert "B_E.png" in os.listdir(), "file not created"

def test_plot_tu():
    pymcabc.DefineProcess("A A > B B", mA=4, mB=10, mC=1, pi=30)
    pymcabc.CrossSection().calc_xsection()
    pymcabc.SaveEvent(100, boolDecay=True, boolDetector=True).to_root(
        "test_eventGen_detector_decay_tu.root"
    )
    pymcabc.PlotData.file("test_eventGen_detector_decay_tu.root")
    assert "B_1_E_decay_A.png" in os.listdir(), "file not created"

