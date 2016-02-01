import json

from model.Cluster import Cluster
from model.Distribution import Distribution


class InputParser:
    def __init__(self, filename):
        self.filename = filename

    def get_dimensions(self):
        with open(self.filename) as file:
            data = json.load(file)
            if data["dimensions"]:
                return data["dimensions"]
            else:
                print("Couldn't find 'dimensions' element in input file")

    def get_clusters(self):
        clusters = []

        with open(self.filename) as file:
            data = json.load(file)
            if data["clusters"]:
                clusters_json = data["clusters"]

                for cluster_json in clusters_json:
                    cluster = Cluster()
                    cluster.set_dimensions(self.get_dimensions())

                    if cluster_json["type"]:
                        type_found = False
                        for distribution in Distribution:
                            if distribution.name == cluster_json["type"]:
                                cluster.set_distribution(Distribution[distribution.name])
                                type_found = True
                        if not type_found:
                            print("Couldn't map distribution type. Defaulting to 'gaussian'")
                    else:
                        print("Couldn't find 'type' element for cluster")

                    if cluster_json["cardinality"]:
                        cardinality = int(cluster_json["cardinality"])
                        if 0 < cardinality <= 10:
                            cluster.set_cardinality(cardinality)
                        else:
                            print("Invalid cardinality. Has to be within 1 to 10. Defaulting to 5.")
                    else:
                        print("Couldn't find 'cardinality' element for cluster")

                    if cluster_json["density"]:
                        density = int(cluster_json["density"])
                        if 0 < density <= 10:
                            cluster.set_density(density)
                        else:
                            print("Invalid density. Has to be within 1 to 10. Defaulting to 5.")
                    else:
                        print("Couldn't find 'density' element for cluster")

                    clusters.append(cluster)
            else:
                print("Couldn't find 'clusters' element in input file")

        return clusters
