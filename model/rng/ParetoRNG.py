import numpy as np

from model.rng.RNG import RNG


class ParetoRNG(RNG):
    def __init__(self, density):
        super().__init__(density)
        self.a, self.m = self.get_mapped_a(density), self.get_mapped_m(density)

    def get_next(self):
        return (np.random.pareto(self.a) + 1) * self.m

    @staticmethod
    def get_mapped_m(density):
        # TODO
        return 3

    @staticmethod
    def get_mapped_a(density):
        # TODO
        return 2
