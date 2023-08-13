from __future__ import annotations

import matplotlib.pyplot as plt

import os, pathlib
import pandas as pd
import uproot


class PlotData:
    """
    class for plotting data
    """

    def plot(data, key):
        plt.hist(data, bins=40, color=None)
        label = key.replace("_", " ")
        plt.xlabel(label)
        plt.ylabel("Events")
        plt.savefig(key + ".png")

    def file(filename="ABC_events.root"):
        if pathlib.PurePosixPath(filename).suffix == ".root":
            file = uproot.open(filename)
            tree = file["events"]
            branches = tree.arrays()
            for key in tree.keys():
                PlotData.plot(branches[key], key)
        elif pathlib.PurePosixPath(filename).suffix == ".root":
            df = pd.read_csv(filename)
            for col in df.columns:
                PlotData.plot(df[col], col)