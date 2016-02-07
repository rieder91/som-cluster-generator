class FileWriter:
    def __init__(self, dataset):
        self.dataset = dataset
        self.output_folder = "output"
        self.default_filename = "clusters"

    def export_for_somtoolbox(self):
        self.create_tv_file("%s/%s.tv" % (self.output_folder, self.dataset.export_name))
        self.create_vec_file("%s/%s.vec" % (self.output_folder, self.dataset.export_name))
        print("Exported to %s/%s" % (self.output_folder, self.dataset.export_name))

    def create_tv_file(self, filename):
        with open(filename, 'w') as file:
            file.write("$TYPE template\n")
            file.write("$XDIM 2\n")
            file.write("$YDIM %s\n" % self.dataset.get_row_count())
            file.write("$VECDIM %s\n" % self.dataset.dimensions)
            for i in range(1, self.dataset.dimensions + 1):
                file.write("%s dummycomponent_%s\n" % (i, i))

    def create_vec_file(self, filename):
        row_cnt = 1
        with open(filename, 'w') as file:
            file.write("$TYPE vec\n")
            file.write("$XDIM %s\n" % self.dataset.get_row_count())
            file.write("$YDIM 1\n")
            file.write("$VEC_DIM %s\n" % self.dataset.dimensions)
            for row in self.dataset.get_rows():
                for item in row:
                    file.write("%s " % float(item))
                file.write("%s" % row_cnt)
                file.write("\n")
                row_cnt += 1
