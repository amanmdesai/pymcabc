import math
import random
import json
import numpy as np
import pymcabc.constants
from pymcabc.particle import Particle


class DecayParticle:
    def __init__(self):
        # self.Ecm = library["Ecm"][0]
        with open("library.json", "r") as f:
            library = json.load(f)
        self.mA = library["mA"][0]
        self.mB = library["mB"][0]
        self.mC = library["mC"][0]
        self.decay_process = library["decay_process"][0]
        self.decay1_mass = library["decay1_mass"][0]
        self.decay2_mass = library["decay2_mass"][0]
        self.massive = library["massive_mass"][0]
        self.delta = pymcabc.constants.delta

    def rotate(self,pdecay: Particle,size: int):

        costh =  (np.random.rand(size) * 2) -1
        sinth = np.sqrt(1 - costh**2)
        phi = 2 * math.pi * np.random.rand(size)
        sinPhi = np.sin(phi)
        cosPhi = np.cos(phi)

        pdecay.px = pdecay.px * cosPhi - pdecay.py * sinPhi
        pdecay.py = pdecay.px * sinPhi + pdecay.py * cosPhi

        pdecay.px = pdecay.px * costh - pdecay.pz * sinth
        pdecay.pz = pdecay.px * sinth + pdecay.pz * costh

        return pdecay


    def decay(self, top: Particle):
        self.decay_p = 1 / (2 * top.mass()) * np.sqrt(
            (self.mA**4+ self.mB**4+ self.mC**4)
            - 2 * (self.mA**2 * self.mB**2 +  self.mA**2 * self.mC**2 + self.mB**2 * self.mC**2)
        )

        decay1 = Particle(-9, -9, -9, -9)
        decay2 = Particle(-9, -9, -9, -9)
        # decay2.mass() = self.decay2_mass

        E1 =  np.sqrt(
            self.decay1_mass * self.decay1_mass + self.decay_p * self.decay_p
        )*np.ones(top.E.shape[0])
        E2 = np.sqrt(
            self.decay2_mass * self.decay2_mass  + self.decay_p * self.decay_p
        )*np.ones(top.E.shape[0])

        decay1.set4momenta(E1, 0, self.decay_p, 0)
        decay2.set4momenta(E2, 0, -self.decay_p, 0)

        decay1 = self.rotate(decay1, size = top.E.shape[0])
        decay2 = self.rotate(decay2, size = top.E.shape[0])

        return decay1, decay2

    def nearlyequal(self,a, b):
        if abs(a - b) < 0.001:
            return True
        else:
            return False

    def prepare_decay(self, top: Particle):
        if self.decay_process != "NaN":
            # decay_process = decay_process.replace(" < "," ")
            # decay_process = decay_process.split(" ")
            #print(top.mass()[0], self.massive)
            if self.nearlyequal(top.mass()[0], self.massive) and top.mass()[0]>(self.decay1_mass + self.decay2_mass):
                decay1, decay2 = self.decay(top)
                decay1 = decay1.boost(top)
                decay2 = decay2.boost(top)
                return decay1, decay2
            else:
                output = np.ones(top.E.size)*(-9)
                decay1 = Particle(output,output, output, output)
                decay2 = Particle(output,output, output, output)
                return decay1, decay2
