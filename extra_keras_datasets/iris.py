"""
  Import the Iris dataset
  Source: http://archive.ics.uci.edu/ml/datasets/Iris
  Description: The data set contains 3 classes of 50 instances each, where
  each class refers to a type of iris plant.

  ~~~ Important note ~~~
  Please cite the following paper when using or referencing the dataset:
  Fisher,R.A. "The use of multiple measurements in taxonomic problems"
  Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions
  to Mathematical Statistics" (John Wiley, NY, 1950).
"""

from tensorflow.keras.utils import get_file
import numpy as np
import math
import logging


def warn_citation():
    """Warns about citation requirements
    # Returns
      Void
    """
    logging.warning(("Please cite the following paper when using or"
                     " referencing this Extra Keras Dataset:"))
    logging.warning(
        ("Fisher,R.A. \"The use of multiple measurements in taxonomic "
         "problems\" Annual Eugenics, 7, Part II, 179-188 (1936); also "
         "in \"Contributions to Mathematical Statistics\" (John Wiley"
         ", NY, 1950).")
      )


def load_data(path="iris.npz", test_split=0.2):
    """Loads the Iris dataset.
    # Arguments
        path: path where to cache the dataset locally
            (relative to ~/.keras/datasets).
        test_split: percentage of data to use for testing (by default 20%)
    # Returns
        Tuple of Numpy arrays: `(input_train, target_train),
                                  (input_test, target_test)`.
        Input structure: (sepal length, sepal width, petal length,
                            petal width)
        Target structure: 0 = iris setosa; 1 = iris versicolor;
                            2 = iris virginica.
    """
    # Log about loading
    logging.basicConfig(level=logging.INFO)
    logging.info('Loading dataset = iris')

    # Load data
    path = get_file(
        path,
        origin=("http://archive.ics.uci.edu/ml/machine-learning-databases/"
                "iris/iris.data")
    )

    # Read data from file
    f = open(path, "r")
    lines = f.readlines()

    # Process each line into input/target structure
    samples = []
    for line in lines:
        sample = line_to_list(line)
        if sample is not None:
            samples.append(sample)
    f.close()

    # Randomly shuffle the data
    np.random.shuffle(samples)

    # Compute test_split in length
    num_test_samples = math.floor(len(samples) * test_split)

    # Split data
    training_data = samples[num_test_samples:]
    testing_data = samples[:num_test_samples]

    # Split into inputs and targets
    input_train = np.array([i[0:4] for i in training_data])
    input_test = np.array([i[0:4] for i in testing_data])
    target_train = np.array([i[4] for i in training_data])
    target_test = np.array([i[4] for i in testing_data])

    # Warn about citation
    warn_citation()

    # Return data
    return (input_train, target_train), (input_test, target_test)


def line_to_list(line):
    """
    Convert a String-based line into a list with input and target data.
    """
    elements = line.split(",")
    if len(elements) > 1:
        target = target_string_to_int(elements[4])
        full_sample = [float(i) for i in elements[0:4]]
        full_sample.append(target)
        return tuple(full_sample)
    else:
        return None


def target_string_to_int(target_value):
    """
    Convert a String-based into an Integer-based target value.
    """
    if target_value == "Iris-setosa\n":
        return 0
    elif target_value == "Iris-versicolor\n":
        return 1
    else:
        return 2
