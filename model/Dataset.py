import math
import random

from model.rng.RNG import RNG
from model.rng.RNGFactory import RNGFactory


class Dataset:
    def __init__(self, dimensions, clusters):
        self.dimensions = dimensions
        self.clusters = clusters
        self.translate_try_count = 2500

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
                cluster.set_values(cluster_values)

    # translation of cluster values to distribute them evenly
    def balance_clusters(self):
        best_distance = 0
        best_centers = [tuple([0] * self.dimensions)]

        for i in range(0, self.translate_try_count):
            centers = []
            for _ in self.clusters:
                center = ()
                for j in range(0, self.dimensions):
                    center += (random.randint(-75, 75),)
                centers.append(center)

            if self.get_sum_of_distances(centers) > best_distance:
                best_distance = self.get_sum_of_distances(centers)
                best_centers = centers

        for i in range(0, len(self.clusters)):
            cluster = self.clusters[i]
            cluster.translate_values(best_centers[i])

    def get_sum_of_distances(self, centers):
        sum = 0
        for center_1 in centers:
            for center_2 in centers:
                if center_1 != center_2:
                    sum += self.get_cluster_distance(center_1, center_2)
        return sum

    @staticmethod
    def get_mapped_cardinality(cardinality):
        # map cardinality
        return 50 * pow(cardinality, 2)

    @staticmethod
    def get_cluster_distance(center_1, center_2):
        # simple euclidean distance
        root_sum = 0
        for i in range(0, len(center_1)):
            p, q = center_1[i], center_2[i]
            root_sum += pow(q - p, 2)
        return math.sqrt(root_sum)
