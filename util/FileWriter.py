class FileWriter:
    def __init__(self, dataset):
        self.dataset = dataset
        self.default_filename = "output.vec"

    def write_to_somtoolbox_file(self, filename=None):
        if not filename:
            print("No filename given - defaulting to %s" % self.default_filename)
            filename = self.default_filename
        row_cnt = 0

        # TODO

        print("Created file %s (%s rows)" % (filename, row_cnt))