import numpy as np

from model.rng.RNG import RNG


class BinomialRNG(RNG):
    def __init__(self, density):
        super().__init__(density)
        self.n, self.p = self.get_mapped_n(density), self.get_mapped_p(density)

    def get_next(self):
        return np.random.binomial(self.n, self.p) - self.n / 2

    @staticmethod
    # number of trials
    def get_mapped_n(density):
        # smaller N means more density
        return (1 / pow(density, 2)) * 750

    @staticmethod
    # probability of each trial
    def get_mapped_p(density):
        # we should probably leave this at 0.5
        return 0.5
