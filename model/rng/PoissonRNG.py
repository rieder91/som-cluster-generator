import numpy as np

from model.rng.RNG import RNG


class PoissonRNG(RNG):
    def __init__(self, density):
        super().__init__(density)
        self.lam = self.get_mapped_lambda(density)

    def get_next(self):
        return np.random.poisson(self.lam)

    @staticmethod
    def get_mapped_lambda(density):
        return (1 / density) * 20
