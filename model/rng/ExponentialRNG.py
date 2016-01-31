import numpy as np

from model.rng.RNG import RNG


class ExponentialRNG(RNG):
    def __init__(self, density):
        super().__init__(density)
        self.scale = self.get_mapped_scale(density)

    def get_next(self):
        return np.random.exponential(self.scale)

    @staticmethod
    def get_mapped_scale(self):
        # 1.0 is default and the higher it gets, the less dense it becomes
        return 5.0
