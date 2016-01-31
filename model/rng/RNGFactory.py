from model.Distribution import Distribution
from model.rng.BinomialRNG import BinomialRNG
from model.rng.ExponentialRNG import ExponentialRNG
from model.rng.GaussianRNG import GaussianRNG
from model.rng.ParetoRNG import ParetoRNG
from model.rng.PoissonRNG import PoissonRNG


class RNGFactory():
    def __init__(self, distribution, cardinality, density):
        self.distribution = distribution
        self.cardinality = cardinality
        self.density = density

    def get_generator(self):
        # instantiate corresponding rng instance and return
        if Distribution.gaussian == self.distribution:
            return GaussianRNG(self.density)
        if Distribution.binomial == self.distribution:
            return BinomialRNG(self.density)
        if Distribution.exponential == self.distribution:
            return ExponentialRNG(self.density)
        if Distribution.pareto == self.distribution:
            return ParetoRNG(self.density)
        if Distribution.poisson == self.distribution:
            return PoissonRNG(self.density)
