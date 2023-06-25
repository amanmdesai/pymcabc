import math
import random
import json
import pymcabc.constants
from pymcabc.particle import Particle


class DecayParticle:
    """
    decays particle
    """

    def __init__(self):
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

    def rotate(self, pdecay: Particle):
        """rotate particle"""
        costh = (random.random * 2) - 1
        sinth = math.sqrt(1 - costh**2)
        phi = 2 * math.pi * random.random()
        sinPhi = math.sin(phi)
        cosPhi = math.cos(phi)

        pdecay.px = pdecay.px * cosPhi - pdecay.py * sinPhi
        pdecay.py = pdecay.px * sinPhi + pdecay.py * cosPhi

        pdecay.px = pdecay.px * costh - pdecay.pz * sinth
        pdecay.pz = pdecay.px * sinth + pdecay.pz * costh

        return pdecay

    def decay(self, top: Particle):
        """decay particle"""
        self.decay_p = (
            1
            / (2 * top.mass())
            * math.sqrt(
                (self.mA**4 + self.mB**4 + self.mC**4)
                - 2
                * (
                    self.mA**2 * self.mB**2
                    + self.mA**2 * self.mC**2
                    + self.mB**2 * self.mC**2
                )
            )
        )

        decay1 = Particle(-9, -9, -9, -9)
        decay2 = Particle(-9, -9, -9, -9)
        # decay2.mass() = self.decay2_mass

        E1 = math.sqrt(
            self.decay1_mass * self.decay1_mass + self.decay_p * self.decay_p
        ) 
        E2 = math.sqrt(
            self.decay2_mass * self.decay2_mass + self.decay_p * self.decay_p
        ) 

        decay1.set4momenta(E1, 0, self.decay_p, 0)
        decay2.set4momenta(E2, 0, -self.decay_p, 0)

        decay1 = self.rotate(decay1)
        decay2 = self.rotate(decay2)

        return decay1, decay2

    def nearlyequal(self, a, b):
        if abs(a - b) < 1e-3:
            return True
        else:
            return False

    def prepare_decay(self, top: Particle):
        if self.decay_process != "NaN":
            # decay_process = decay_process.replace(" < "," ")
            # decay_process = decay_process.split(" ")
            # print(top.mass()[0], self.massive)
            if self.nearlyequal(top.mass(), self.massive) and top.mass() > (
                self.decay1_mass + self.decay2_mass
            ):
                decay1, decay2 = self.decay(top)
                decay1 = decay1.boost(top)
                decay2 = decay2.boost(top)
                return decay1, decay2
            else:
                output = -9
                decay1 = Particle(output, output, output, output)
                decay2 = Particle(output, output, output, output)
                return decay1, decay2
