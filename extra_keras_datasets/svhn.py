"""
  Import the SVHN dataset
  Source: http://ufldl.stanford.edu/housenumbers/
  Description: Street View House Numbers

  ~~~ Important note ~~~
  Please cite the following paper when using or referencing the dataset:
  Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu,
  Andrew Y. Ng Reading Digits in Natural Images with Unsupervised Feature
  Learning NIPS Workshop on Deep Learning and Unsupervised Feature
  Learning 2011. Retrieved from
  http://ufldl.stanford.edu/housenumbers/nips2011_housenumbers.pdf

"""

from tensorflow.keras.utils import get_file
import numpy as np
from scipy import io as sio
import logging


def warn_citation():
    """Warns about citation requirements
    # Returns
      Void
    """
    logging.warning(("Please cite the following paper when using or"
                     " referencing this Extra Keras Dataset:"))
    logging.warning(
        ("Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Bo Wu, "
         "Andrew Y. Ng Reading Digits in Natural Images with Unsupervised "
         "Feature Learning NIPS Workshop on Deep Learning and Unsupervised "
         "Feature Learning 2011. Retrieved from "
         "http://ufldl.stanford.edu/housenumbers/nips2011_housenumbers.pdf")
      )
    logging.warning(("Noncommercial use is allowed only: see the "
                     "SVHN website for more information."))


def load_data(path="svhn_matlab.npz", type="normal"):
    """Loads the SVHN dataset.
    # Arguments
        path: path where to cache the dataset locally
            (relative to ~/.keras/datasets).
        type: any of normal,
                extra (extra appends ~530K extra images for training)
    # Returns
        Tuple of Numpy arrays: `(input_train, target_train),
                                  (input_test, target_test)`.
    """
    # Log about loading
    logging.basicConfig(level=logging.INFO)
    logging.info('Loading dataset = svhn')

    # Load data
    path_train = get_file(
        f"{path}_train", origin=("http://ufldl.stanford.edu/housenumbers/"
                                 "train_32x32.mat")
    )
    path_test = get_file(
        f"{path}_test", origin=("http://ufldl.stanford.edu/housenumbers/"
                                "test_32x32.mat")
    )

    # Load data from Matlab file.
    # Source: https://stackoverflow.com/a/53547262
    mat_train = sio.loadmat(path_train)
    mat_test = sio.loadmat(path_test)

    # Prepare training data
    input_train = mat_train["X"]
    input_train = np.rollaxis(input_train, 3, 0)
    target_train = mat_train["y"].flatten()

    # Prepare testing data
    input_test = mat_test["X"]
    input_test = np.rollaxis(input_test, 3, 0)
    target_test = mat_test["y"].flatten()

    # Append extra data, if required
    if type == "extra":
        path_extra = get_file(
            f"{path}_extra",
            origin="http://ufldl.stanford.edu/housenumbers/extra_32x32.mat",
        )
        mat_extra = sio.loadmat(path_extra)
        input_extra = mat_extra["X"]
        input_extra = np.rollaxis(input_extra, 3, 0)
        target_extra = mat_extra["y"].flatten()
        input_train = np.concatenate((input_extra, input_train))
        target_train = np.concatenate((target_extra, target_train))

    # Warn about citation
    warn_citation()

    # Return data
    return (input_train, target_train), (input_test, target_test)
