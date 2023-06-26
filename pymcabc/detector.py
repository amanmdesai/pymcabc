import random
import math
from pymcabc.particle import Particle


class Detector:
    """Applies gaussian smearing on E and momenta"""

    def __init__(self, sigma: float = 1.0, factor: float = 1.0):
        self.sigma = sigma
        self.factor = factor

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
            output_px = [0] * len(particle.px)
            output_py = [0] * len(particle.px)
            output_pz = [0] * len(particle.px)
            output_E = [0] * len(particle.px)
            for i in range(len(particle.px)):
                """
                momentum = math.sqrt(
                    particle.px[i] ** 2 + particle.py[i] ** 2 + particle.pz[i] ** 2
                )
                random_measure_momentum = (
                    random.gauss(momentum, self.factor * self.sigma) / momentum
                )
                random_measure_energy = (
                    random.gauss(particle.E[i], self.sigma) / particle.E[i]
                )

                output_px[i] = random_measure_momentum * particle.px[i]
                output_py[i] = random_measure_momentum * particle.py[i]
                output_pz[i] = random_measure_momentum * particle.pz[i]
                output_E[i] = random_measure_energy * particle.E[i]
                """

                output_px[i] = random.gauss(particle.px[i], self.factor*self.sigma)
                output_py[i] = random.gauss(particle.py[i], self.factor*self.sigma)
                output_pz[i] = random.gauss(particle.pz[i], self.factor*self.sigma)
                output_E[i] = random.gauss(particle.E[i], self.sigma)
                
            particle_output = Particle(output_E, output_px, output_py, output_pz)
        return particle_output

#mass = output_E[i] ** 2 - (output_px[i] ** 2 + output_py[i] ** 2 + output_pz[i] ** 2)

