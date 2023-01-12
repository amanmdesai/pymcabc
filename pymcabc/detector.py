import numpy as np
from pymcabc.particle import Particle


class Detector:
    """Applies gaussian smearing on E and momenta"""
    def identify_smear(particle: Particle, type: str = "gauss"):
        if type == "gauss":
            particle = self.gauss_smear(particle)
        else:
            print("Type Not found")
        return particle
    def gauss_smear(self, particle: Particle, mean: float = 1, sigma: float = 0.05):
        size=particle.E.shape[0]
        if particle.px[0] ==-9 and particle.py[0] == -9:
            return particle
        else:
            particle.px = particle.px*np.random.normal(mean,sigma,size)
            particle.py = particle.px*np.random.normal(mean,sigma,size)
            particle.pz = particle.px*np.random.normal(mean,sigma,size)
            particle.E = particle.E*np.random.normal(mean,sigma,size)
        return particle
