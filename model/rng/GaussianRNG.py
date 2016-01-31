import numpy as np

from model.rng.RNG import RNG


class GaussianRNG(RNG):
    def __init__(self, density):
        super().__init__(density)
        self.mu, self.sigma = 0, self.get_mapped_sigma(density)

    def get_next(self):
        return np.random.normal(self.mu, self.sigma)

    @staticmethod
    def get_mapped_sigma(density):
        # TODO
        return 3.0
