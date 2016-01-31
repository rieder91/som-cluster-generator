from model.rng.RNG import RNG
from model.rng.RNGFactory import RNGFactory


class Dataset:
    def __init__(self, dimensions, clusters):
        self.dimensions = dimensions
        self.clusters = clusters
        self.values = [None] * dimensions

    def generate_values(self):
        for cluster in self.clusters:
            print("Generating values for cluster %s" % cluster)

            rngFactory = RNGFactory(cluster.distribution, cluster.cardinality, cluster.density)
            rng = rngFactory.get_generator()

            if isinstance(rng, RNG):
                cluster_values = []
                for n in range(0, self.get_mapped_cardinality(cluster.cardinality)):
                    row = ()
                    for i in range(0, self.dimensions):
                        row += (rng.get_next(),)
                    cluster_values.append(row)
                self.values[self.clusters.index(cluster)] = cluster_values

                # TODO translation of cluster values

                print(self.values)

    @staticmethod
    def get_mapped_cardinality(cardinality):
        # TODO map cardinality properly
        return 100
