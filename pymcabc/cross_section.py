import random
import math
import pymcabc.constants
import json


class MatrixElement:
    def __init__(self):
        with open("library.json", "r") as f:
            library = json.load(f)
        self.m1 = library["m1"][0]
        self.m2 = library["m2"][0]
        self.m3 = library["m3"][0]
        self.m4 = library["m4"][0]
        self.mx = library["mx"][0]
        self.Ecm = library["Ecm"][0]
        self.g = pymcabc.constants.g
        self.pi = pymcabc.constants.pi
        self.delta = pymcabc.constants.delta
        self.p_i = math.sqrt((self.Ecm / 2) ** 2 - (self.m1) ** 2)

    def s_channel(self):
        """definition for s channel"""
        return (self.g**2) / (self.Ecm**2 - self.mx**2)

    def t_channel(self, costh, pf):
        """definition for t channel"""
        deno = (
            self.m1**2
            + self.m3**2
            - self.mx**2
            - (self.Ecm * math.sqrt(pf**2 + self.m3**2))
            + (2 * self.p_i * pf * costh)
        )
        if abs(deno) <= 0.09:
            return (self.g**2) / (deno + 100)
        else:
            return (self.g**2) / deno

    def u_channel(self, costh, pf):
        """definition for u channel"""
        deno = (
            self.m1**2
            + self.m4**2
            - self.mx**2
            - (self.Ecm * math.sqrt(pf**2 + self.m4**2))
            - (2 * self.p_i * pf * costh)
        )
        if abs(deno) <= 0.09:
            return (self.g**2) / (deno + 100)
        else:
            return (self.g**2) / deno


class CrossSection:
    def __init__(self):
        self.pi = pymcabc.constants.pi
        self.delta = pymcabc.constants.delta
        with open("library.json", "r") as f:
            library = json.load(f)
        self.Ecm = library["Ecm"][0]
        self.m1 = library["m1"][0]
        self.m3 = library["m3"][0]
        self.m4 = library["m4"][0]
        self.process = library["process_type"][0]
        self.p_f = pymcabc.constants.outgoing_p(self.Ecm, self.m3, self.m4)
        self.p_i = math.sqrt((self.Ecm / 2) ** 2 - (self.m1) ** 2)

    def dsigma_st(self, costh):
        ME = MatrixElement().s_channel() + MatrixElement().t_channel(costh, self.p_f)
        dsigma_st = 1 / ((8 * self.Ecm * self.pi) ** 2)
        dsigma_st = dsigma_st * abs(self.p_f / self.p_i) * ME**2
        return dsigma_st

    def dsigma_tu(self, costh):
        ME = MatrixElement().t_channel(costh, self.p_f) + MatrixElement().u_channel(costh, self.p_f)
        dsigma_tu = 0.5 / ((self.Ecm * 8 * self.pi) ** 2)
        dsigma_tu = dsigma_tu * abs(self.p_f / self.p_i) * ME**2
        return dsigma_tu

    def xsection(self, w_max):
        costh = -1 + random.random() * self.delta
        if self.process == "st":
            w_i = CrossSection().dsigma_st(costh) * self.delta
        elif self.process == "tu":
            w_i = CrossSection().dsigma_tu(costh) * self.delta
        if w_max < w_i:
            w_max = w_i
        return w_i, w_max

    def integrate_xsec(self, N=80000):
        w_sum = 0
        w_max = 0
        w_square = 0
        for _i in range(N):
            w_i, w_max = CrossSection().xsection(w_max)
            w_sum += w_i
            w_square += w_i * w_i
        with open("library.json", "r") as f:
            library = json.load(f)
        library["w_max"].append(w_max)
        library["w_square"].append(w_square)
        library["w_sum"].append(w_sum)
        with open("library.json", "w") as f:
            json.dump(library, f)
        return None

    def calc_xsection(self, N=80000):
        self.integrate_xsec(N)
        with open("library.json", "r") as f:
            library = json.load(f)
        w_sum = library["w_sum"][0]
        w_square = library["w_square"][0]
        w_max = library["w_max"][0]
        sigma_x = w_sum * pymcabc.constants.convert / (N * 1e12)
        variance = math.sqrt(w_square / N - (w_sum / N) ** 2)  # barn unit
        error = (
            variance * pymcabc.constants.convert / (math.sqrt(N) * 1e12)
        )  # barn unit
        return sigma_x, error
