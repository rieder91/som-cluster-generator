from model.Distribution import Distribution
import operator

class Cluster:
    def __init__(self, distribution=Distribution.gaussian, cardinality=5, density=5):
        self.distribution = distribution
        self.cardinality = cardinality
        self.density = density
        self.values = []
        self.center = ()

    def set_distribution(self, distribution):
        self.distribution = distribution

    def set_cardinality(self, cardinality):
        self.cardinality = cardinality

    def set_density(self, density):
        self.density = density

    def set_dimensions(self, dimensions):
        self.center = tuple([0] * dimensions)

    def set_values(self, values):
        self.values = values

    def translate_values(self, trans):
        self.center = tuple(map(operator.add, self.center, trans))
        for i in range(0, len(self.values)):
            row = self.values[i]
            new_row = ()
            for j in range(0, len(row)):
                new_row += (row[j] + trans[j],)
            self.values[i] = new_row

    def __str__(self):
        return "distribution=%s, cardinality=%s, density=%s" % (self.distribution.name, self.cardinality, self.density)
