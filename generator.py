import sys

from util.FileWriter import FileWriter
from util.InputParser import InputParser
from util.Plotter import Plotter
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
            print()

            inputParser = InputParser(inputfile)
            dimensions = inputParser.get_dimensions()
            clusters = inputParser.get_clusters()
            export_name = inputParser.get_export_name()

            print("Dimensions = %s" % dimensions)
            print("Cluster count = %s" % len(clusters))
            for cluster in clusters:
                print(" - %s" % cluster)
            print()

            dataset = Dataset(dimensions, clusters, export_name)
            print("Generating random values for clusters...")
            dataset.generate_values()
            print("Balancing clusters... (this may take a while)")
            dataset.balance_clusters()
            print()

            filewriter = FileWriter(dataset)
            print("Writing SOMToolbox files...")
            filewriter.export_for_somtoolbox()

            if 1 <= dimensions <= 2:
                print()
                print("Input has <= 2 dimensions - showing plot")
                plotter = Plotter(dataset)
                plotter.plot()
