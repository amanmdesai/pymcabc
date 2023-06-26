from __future__ import annotations

import matplotlib.pyplot as plt

# import pandas as pd
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
        file = uproot.open(filename)
        tree = file["events"]
        branches = tree.arrays()
        for key in tree.keys():
            PlotData.plot(branches[key], key)

