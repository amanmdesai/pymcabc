import math
import random
import json
import numpy as np
import pymcabc.constants
from pymcabc.cross_section import CrossSection


class GENEvents:
    """
    internal class for generating events
    """

    def __init__(self, Nevent: int):
        self.delta = pymcabc.constants.delta
        self.Nevent = Nevent
        with open("library.json", "r") as f:
            library = json.load(f)
        self.w_max = library["w_max"][0]
        self.Ecm = library["Ecm"][0]
        self.m3 = library["m3"][0]
        self.m4 = library["m4"][0]
        self.process = library["process_type"][0]
        self.out_p = library["outgoing_p"][0]

    def gen_events(self):
        i = 0
        prob = 0
        m_costh = np.zeros(self.Nevent)
        p1_px = np.zeros(self.Nevent)
        p1_py = np.zeros(self.Nevent)
        p1_pz = np.zeros(self.Nevent)
        p1_e = np.zeros(self.Nevent)
        p2_px = np.zeros(self.Nevent)
        p2_py = np.zeros(self.Nevent)
        p2_pz = np.zeros(self.Nevent)
        p2_e = np.zeros(self.Nevent)
        while i < self.Nevent:
            costh = -1 + (random.random() * self.delta)
            phi = 2 * math.pi * random.random()  # * self.delta
            if self.process == "st":
                w_ii = CrossSection().dsigma_st(costh) * self.delta
            elif self.process == "tu":
                w_ii = CrossSection().dsigma_tu(costh) * self.delta
            prob = w_ii / self.w_max
            random_point = random.random()
            if random_point < prob:
                m_costh[i] = math.degrees(math.acos(costh))
                sinth = math.sqrt(1 - costh**2)
                p1_e[i] = math.sqrt(self.out_p * self.out_p + self.m3 * self.m3)
                p1_px[i] = self.out_p * sinth * math.cos(phi)
                p1_py[i] = self.out_p * sinth * math.sin(phi)
                p1_pz[i] = self.out_p * costh
                p2_e[i] = math.sqrt(self.out_p * self.out_p + self.m4 * self.m4)
                p2_px[i] = -p1_px[i]
                p2_py[i] = -p1_py[i]
                p2_pz[i] = -p1_pz[i]
                i = i + 1
                if i % 100 == 0:
                    print("generating event ", i, " of ", self.Nevent)
        return p1_e, p1_px, p1_py, p1_pz, p2_e, p2_px, p2_py, p2_pz
