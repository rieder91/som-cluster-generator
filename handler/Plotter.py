import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, dataset):
        self.dataset = dataset

    def plot(self):
        size = 0
        for cluster in self.dataset.clusters:
            size += len(cluster.values)

        print("Plotting %s points in total" % size)

        x = np.zeros(size)
        y = np.zeros(size)

        i = 0
        for cluster in self.dataset.clusters:
            for value in cluster.values:
                x[i] = float(value[0])
                if len(value) == 2:
                    y[i] = float(value[1])
                i += 1

        print(x)
        print(y)

        plt.plot(x, y, 'k,', markersize=1, marker='o')
        axes = plt.gca()
        axes.set_xlim([-100, 100])
        axes.set_ylim([-100, 100])
        plt.show()
