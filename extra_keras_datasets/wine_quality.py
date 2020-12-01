"""
  Import the Wine Quality dataset
  Source: https://archive.ics.uci.edu/ml/datasets/wine+quality
  Description: Two datasets are included, related to red and white vinho
  verde wine samples, from the north of Portugal.
  The goal is to model wine quality based on physicochemical tests.

  ~~~ Important note ~~~
  Please cite the following paper when using or referencing the dataset:
  P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
  Modeling wine preferences by data mining from physicochemical
  properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.
"""

from tensorflow.keras.utils import get_file
import numpy as np
import logging
import pandas as pd
from sklearn.model_selection import train_test_split


def warn_citation():
    """Warns about citation requirements
    # Returns
      Void
    """
    logging.warning(("Please cite the following paper when using or"
                     " referencing this Extra Keras Dataset:"))
    logging.warning(
        ("P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. "
         "Modeling wine preferences by data mining from physicochemical "
         "properties. In Decision Support Systems, Elsevier, "
         "47(4):547-553, 2009.")
      )


def load_data(
    path_red="wine-quality-red.csv",
    path_white="wine-quality-white.csv",
    test_split=0.2,
    which_data='both',
    shuffle=True
):
    """Loads the Wine Quality dataset.
    # Arguments
        path_red: path where to cache the red wines dataset locally
            (relative to ~/.keras/datasets).
        path_white: path where to cache the white wines dataset locally
            (relative to ~/.keras/datasets).
        test_split: percentage of data to use for testing (by default 20%)
        which_data: wine type to return. Can be 'white', 'red', or 'both'.
        shuffle: whether to shuffle the data when generating train/test
            split.
    # Returns
        Tuple of Numpy arrays: `(input_train, target_train),
                                  (input_test, target_test)`.
        Input structure: (fixed acidity, volatile acidity, citric acid,
                          residual sugar, chlorides, free sulfur diox-
                          ide, total sulfur dioxide, density, pH, sul-
                          phates, alcohol, wine type)
        Target structure: quality score between 0 and 10

    """
    # Log about loading
    logging.basicConfig(level=logging.INFO)
    logging.info('Loading dataset = wine_quality')

    # Assert data
    assert which_data in ['red', 'white', 'both']

    # Download data
    path_white = get_file(
        path_white,
        origin=("https://archive.ics.uci.edu/ml/machine-learning-"
                "databases/wine-quality/winequality-white.csv")
    )
    path_red = get_file(
        path_red,
        origin=("https://archive.ics.uci.edu/ml/machine-learning-"
                "databases/wine-quality/winequality-red.csv")
    )

    # Process white data
    white = pd.read_csv(path_white, header=0, delimiter=';')
    white.insert(11, 'type', 'white')
    white = white.to_numpy()
    white_samples = white[:, 0:12]
    white_targets = white[:, 12]

    # Process red data
    red = pd.read_csv(path_red, header=0, delimiter=';')
    red.insert(11, 'type', 'red')
    red = red.to_numpy()
    red_samples = red[:, 0:12]
    red_targets = red[:, 12]

    # Specify dataset before train/test split generation
    if which_data == 'red':
        samples = red_samples
        targets = red_targets
    elif which_data == 'white':
        samples = white_samples
        targets = white_targets
    else:
        samples = np.concatenate((red_samples, white_samples))
        targets = np.concatenate((red_targets, white_targets))

    # Generate train/test split
    input_train, input_test, target_train, target_test = \
        train_test_split(samples, targets, test_size=test_split,
                         shuffle=shuffle)

    # Warn about citation
    warn_citation()

    # Return data
    return (input_train, target_train), (input_test, target_test)
