from model.Distribution import Distribution


class Cluster:
    def __init__(self, distribution=Distribution.gaussian, cardinality=5, density=5):
        self.distribution = distribution
        self.cardinality = cardinality
        self.density = density

    def set_distribution(self, distribution):
        self.distribution = distribution

    def set_cardinality(self, cardinality):
        self.cardinality = cardinality

    def set_density(self, density):
        self.density = density

    def __str__(self):
        return "distribution=%s, cardinality=%s, density=%s" % (self.distribution.name, self.cardinality, self.density)
