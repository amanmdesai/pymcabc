import math
import numpy as np


class Particle:
    """
    This class assigns four momentum to a particle

    Parameters:
        E (float): Energy of the particle
        px (float): x momentum of the particle
        py (float): y momentum of the particle
        pz (float): z momentum of the particle

    """

    def __init__(self, E: float, px: float, py: float, pz: float):
        """
        Assigns four momentum to a particle

        Parameters:
            E (float): Energy of the particle
            px (float): x momentum of the particle
            py (float): y momentum of the particle
            pz (float): z momentum of the particle

        """
        self.E = E
        self.px = px
        self.py = py
        self.pz = pz

    def E(self):
        """returns particle's energy"""
        return self.E

    def px(self):
        """returns x component of particle's momentum"""
        return self.px

    def py(self):
        """returns y component of particle's momentum"""
        return self.py

    def pz(self):
        """returns z component of particle's momentum"""
        return self.pz

    def p(self):
        """returns particle's absolute momentum"""
        return np.sqrt(self.px**2 + self.py**2 + self.pz**2)

    def p2(self):
        """returns square of particle's absolute momentum"""
        return self.px**2 + self.py**2 + self.pz**2

    def pT(self):
        """returns particle's transverse momentum"""
        return np.sqrt(self.px**2 + self.py**2)

    def mass(self):
        """returns particle's mass"""
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
        """assign new four momentum to an existing particle"""
        self.px = new_px
        self.py = new_py
        self.pz = new_pz
        self.E = new_E

    def boost(self, other):
        """
        boosts a particle four momentum.
         # boost motivated from ROOT TLorentzVector class

         other is used to boost
        """
        new = Particle(0., 0., 0., 0.)
        new_other = Particle(0., 0., 0., 0.)
        
        new_other.set4momenta(
            other.E, other.px / other.E, other.py / other.E, other.pz / other.E
        )
        beta = new_other.p2()
        gamma = 1.0 / math.sqrt(1.0 - beta)

        if beta>0:
            gamma_2 = (gamma - 1.0) / beta
        else:
            gamma_2 = 0.0


        dotproduct = (
            self.px * new_other.px + self.py * new_other.py + self.pz * new_other.pz
        )
        new.px = self.px + (gamma_2 * dotproduct + gamma * self.E) * new_other.px
        new.py = self.py + (gamma_2 * dotproduct + gamma * self.E) * new_other.py
        new.pz = self.pz + (gamma_2 * dotproduct + gamma * self.E) * new_other.pz
        new.E = gamma * (self.E + dotproduct)
        return new