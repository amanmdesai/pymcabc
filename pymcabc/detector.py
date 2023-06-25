import random
from pymcabc.particle import Particle


class Detector:
    """Applies gaussian smearing on E and momenta"""
    def __init__(self, sigma: float =0.1):
        self.sigma = sigma

    def identify_smear(self, particle: Particle, type: str = "gauss"):
        if type == "gauss":
            particle = self.gauss_smear(particle)
        else:
            print("Type Not found")
        return particle

    def gauss_smear(self, particle: Particle):
        if particle.px[0] == -9 and particle.py[0] == -9:
            return particle
        else:
            output_px = [0]*len(particle.px)
            output_py = [0]*len(particle.px)
            output_pz = [0]*len(particle.px)
            output_E = [0]*len(particle.px)
            for i in range(len(particle.px)):
                output_px[i] = random.gauss(particle.px[i], self.sigma)
                output_py[i] = random.gauss(particle.py[i], self.sigma)
                output_pz[i] = random.gauss(particle.pz[i], self.sigma)
                output_E[i] = random.gauss(particle.E[i], self.sigma)
        
            particle_output = Particle(output_px, output_py, output_pz, output_E)

        return particle_output
