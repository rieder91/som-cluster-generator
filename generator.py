import sys

from model.Dataset import Dataset
from util.FileWriter import FileWriter
from util.InputParser import InputParser
from util.Plotter import Plotter


def get_inputfile():
    if len(sys.argv) >= 2:
        return sys.argv[1].strip()
    else:
        return None


def get_quiet_mode():
    if len(sys.argv) == 3:
        return "-q" == sys.argv[2].strip()
    return False


def print_help():
    print("Usage: python generator.py <input-file> [options...]")
    print("Options:")
    print("    -q  Do not show plot if dimensions is <= 2")
    print("")
    print("Expected format of input-file:")
    print("""
    {
        "dimensions": <dimensions>,
        "export_name": "<export_name>",
        "clusters": [
            {
            "type": "<type>",
            "cardinality": "<cardinality>",
            "density": "<density>"
            },
            ...
        ]
    }
    """)
    print("<dimensions>  - number of dimensions to use; >= 1")
    print("<export_name> - the name of the file the results are written to")
    print("<type>        - one of 'binomial', 'exponential', 'gaussian', 'pareto','poisson'")
    print("<cardinality> - ranges from 1 (low) to 10 (high))")
    print("<density>     - ranges from 1 (low) to 10 (high))")
    print("")


if __name__ == "__main__":
    inputfile = get_inputfile()
    quiet_mode = get_quiet_mode()
    if inputfile is None:
        print_help()
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

        if 1 <= dimensions <= 2 and not quiet_mode:
            print()
            print("Input has <= 2 dimensions - showing plot")
            plotter = Plotter(dataset)
            plotter.plot()
