# SOMToolbox Dataset Generator - Clusters

## Built With

 * Python 3.5.1
 * [NumPy 1.10.4](http://www.numpy.org/)
 * [matplotlib](http://matplotlib.org/)

## Purpose

This script generates datasets to be used with the [SOMToolbox](http://www.ifs.tuwien.ac.at/dm/somtoolbox/). The focus is on clusters. The following settings can be configured:

 * name of the output files
 * number of dimensions
 * number of clusters
 * for each cluster:
  * distribution type
  * cardinality
  * density

Both the cardinality and density range from 1 (low) to 10 (high). The following distribution types are supported:

 * Binomial
 * Exponential
 * Gaussian
 * Pareto
 * Poisson
 
If the program is run with <= 2 dimensions it will also display a plot of the data.

The resulting vector and template vector files can be used by the SOMToolbox to train a SOM. The goal is to analyze the resulting maps and visualize how different cluster configuration can be detected.
 
## Running the program

First you'll want to install the dependencies. Afterwards you can run the program itself:

```
pip install -r requirements.txt
python generator.py <path-to-input-file>
```

In case the installation of the dependencies doesn't work out-of-the-box, they can also be installed manually:

 * [numpy](https://docs.scipy.org/doc/numpy-1.10.1/user/install.html)
 * [matplotlib](http://matplotlib.org/users/installing.html)


The input file is a JSON file. The format should be self-explanatory given an example:

```
{
  "dimensions": 2,
  "export_name": "example1",
  "clusters": [
    {
      "type": "binomial",
      "cardinality": "4",
      "density": "8"
    },
    {
      "type": "exponential",
      "cardinality": "5",
      "density": "7"
    },
    {
      "type": "pareto",
      "cardinality": "9",
      "density": "6"
    },
    {
      "type": "poisson",
      "cardinality": "9",
      "density": "2"
    },
    {
      "type": "gaussian",
      "cardinality": "3",
      "density": "10"
    }
  ]
}
```

The results are written to the ``output`` folder with the name configured in the input file.
