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
        costh = (2 * random.random()) - 1
        sinth = math.sqrt(1 - costh**2)
        phi = 2 * math.pi * random.random()
        sinPhi = math.sin(phi)
        cosPhi = math.cos(phi)
        pdecay_out = Particle(0, 0, 0, 0)
        pdecay_out.px = pdecay.pz * sinth * cosPhi
        pdecay_out.py = pdecay.pz * sinth * sinPhi
        pdecay_out.pz = pdecay.pz * costh
        pdecay_out.E = pdecay.E

        return pdecay_out

    def decay(self, top: Particle):
        """decay particle"""

        E1 = (top.mass() ** 2 - self.decay2_mass**2 + self.decay1_mass**2) / (
            2 * top.mass()
        )

        E2 = top.mass() - E1

        self.decay_p = math.sqrt(
            (top.mass() ** 2 - (self.decay1_mass + self.decay2_mass) ** 2)
            * (top.mass() ** 2 - (self.decay1_mass - self.decay2_mass) ** 2)
        ) / (2 * top.mass())

        """ 
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

        # decay2.mass() = self.decay2_mass

        E1 = math.sqrt(
            self.decay1_mass * self.decay1_mass + self.decay_p * self.decay_p
        ) 
        E2 = math.sqrt(
            self.decay2_mass * self.decay2_mass + self.decay_p * self.decay_p
        ) 
        """

        decay1 = Particle(0, 0, 0, 0)
        decay2 = Particle(0, 0, 0, 0)

        decay1.set4momenta(E1, 0, 0, self.decay_p)
        decay2.set4momenta(E2, 0, 0, -self.decay_p)

        decay1 = self.rotate(decay1)
        decay2.set4momenta(E2, -decay1.px, -decay1.py, -decay1.pz)
        # decay2 = self.rotate(decay2)

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
            decay_array1_px = [0] * len(top.px)
            decay_array1_py = [0] * len(top.px)
            decay_array1_pz = [0] * len(top.px)
            decay_array1_E = [0] * len(top.px)

            decay_array2_px = [0] * len(top.px)
            decay_array2_py = [0] * len(top.px)
            decay_array2_pz = [0] * len(top.px)
            decay_array2_E = [0] * len(top.px)

            for i in range(len(top.px)):
                heavy_state = Particle(top.E[i], top.px[i], top.py[i], top.pz[i])
                if self.nearlyequal(
                    heavy_state.mass(), self.massive
                ) and heavy_state.mass() > (self.decay1_mass + self.decay2_mass):
                    decay1, decay2 = self.decay(heavy_state)
                    decay1 = decay1.boost(heavy_state)
                    decay2 = decay2.boost(heavy_state)

                    decay_array1_px[i] = decay1.px
                    decay_array1_py[i] = decay1.py
                    decay_array1_pz[i] = decay1.pz
                    decay_array1_E[i] = decay1.E

                    decay_array2_px[i] = decay2.px
                    decay_array2_py[i] = decay2.py
                    decay_array2_pz[i] = decay2.pz
                    decay_array2_E[i] = decay2.E
                else:
                    output = -9
                    decay_array1_px[i] = output
                    decay_array1_py[i] = output
                    decay_array1_pz[i] = output
                    decay_array1_E[i] = output

                    decay_array2_px[i] = output
                    decay_array2_py[i] = output
                    decay_array2_pz[i] = output
                    decay_array2_E[i] = output

            decay1 = Particle(
                decay_array1_E, decay_array1_px, decay_array1_py, decay_array1_pz
            )
            decay2 = Particle(
                decay_array2_E, decay_array2_px, decay_array2_py, decay_array2_pz
            )
            return decay1, decay2
