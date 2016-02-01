import sys

from handler.InputParser import InputParser
from handler.Plotter import Plotter
from model.Dataset import Dataset


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

            print("Generating random values for clusters...")
            dataset.generate_values()
            print("Balancing clusters...")
            dataset.balance_clusters()

            if 1 <= dimensions <= 2:
                print("Input has <= 2 dimensions - showing plot")
                plotter = Plotter(dataset)
                plotter.plot()
