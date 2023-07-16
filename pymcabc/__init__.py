"""
Copyright (c) 2023 Aman Desai. All rights reserved.
"""


from pymcabc.identify_process import DefineProcess
from pymcabc.cross_section import MatrixElement, CrossSection
from pymcabc.save_events import SaveEvent
from pymcabc.generate_event import GENEvents
from pymcabc.plotting import PlotData
from pymcabc.feynman_diagram import FeynmanDiagram
from pymcabc.particle import Particle



def convert_tocsv(inputname: str ="input.root", outputname: str ="filename.csv"):
    import os
    import uproot
    import pandas as pd

    """function to save events as CSV file
    Parameters:
        name (str): name of csv file

    """

    check_extension_input = os.path.splitext(inputname)
    if check_extension_input[1] != ".root":
        raise ValueError("Input supported with .root extension only") 

    check_extension_output = os.path.splitext(outputname)
    if check_extension_output[1] != ".csv":
        raise ValueError("Output supported with .csv extension only") 

    data = uproot.open(inputname)["events"]
    df = pd.DataFrame(columns=data.keys())
    for column in df.columns:
        df[column] = data[column].array().to_numpy()
    df.to_csv(outputname)