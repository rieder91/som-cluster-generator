import sys

from model.Dataset import Dataset
from parse.InputParser import InputParser


def get_inputfile():
    if len(sys.argv) == 2:
        return sys.argv[1].strip()
    else:
        return None


def print_help():
    # TODO
    pass


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print_help()
    else:
        inputfile = get_inputfile()
        if inputfile is None:
            # TODO
            print("Going interactive")
        else:
            print("Loading configuration from file %s" % inputfile)
            inputParser = InputParser(inputfile)
            dimensions = inputParser.get_dimensions()
            clusters = inputParser.get_clusters()

            print("Dimensions = %s" % dimensions)
            print("Cluster count = %s" % len(clusters))
            for cluster in clusters:
                print(" - %s" % cluster)
            print()

            dataset = Dataset(dimensions, clusters)
            dataset.generate_values()
