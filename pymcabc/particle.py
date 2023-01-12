import math
import numpy as np

class Particle:
    def __init__(self, E, px, py, pz):
        # self.id = id
        self.E = E
        self.px = px
        self.py = py
        self.pz = pz

    # def id(self):
    #    return self.id

    def E(self):
        return self.E

    def px(self):
        return self.px

    def py(self):
        return self.py

    def pz(self):
        return self.pz

    def p(self):
        return np.sqrt(self.px**2 + self.py**2 + self.pz**2)

    def p2(self):
        return self.px**2 + self.py**2 + self.pz**2

    def pT(self):
        return np.sqrt(self.px**2 + self.py**2)


    def mass(self):
        # try:
        #    x = math.sqrt(self.E**2 - sum([self.px**2, self.py**2, self.pz**2]))
        #    return x
        # except:
        #    return 0
        x = self.E**2 - self.px**2 - self.py**2 - self.pz**2
        if x[0] < 0:
            x = np.zeros(self.E.size())
        else:
            x = np.sqrt(x)
        return x

    def set4momenta(self, new_E, new_px, new_py, new_pz):
        self.px = new_px
        self.py = new_py
        self.pz = new_pz
        self.E = new_E

    def boost(self, other):  # boost motivated from ROOT TLorentzVector class
        new = Particle(-9,-9,-9,-9)
        other.set4momenta(other.E, other.px/other.E,other.py/other.E,other.pz/other.E)
        beta = other.p()
        gamma = 1.0 /np.sqrt(1 - beta**2)
        gamma_2 = (gamma - 1.0) / beta

        dotproduct = (
            self.px * other.px + self.py * other.py + self.pz * other.pz
        )
        new.px =  self.px + (gamma_2 * dotproduct + gamma * self.E)*other.px
        new.py =  self.py + (gamma_2 * dotproduct + gamma * self.E)*other.py
        new.pz =  self.pz + (gamma_2 * dotproduct + gamma * self.E)*other.pz
        new.E = gamma * (self.E + dotproduct)
        return new
