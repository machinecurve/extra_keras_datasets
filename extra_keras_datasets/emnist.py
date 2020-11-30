"""
  Import the EMNIST dataset
  Source: https://www.nist.gov/itl/products-and-services/emnist-dataset
  Description: The EMNIST dataset is a set of handwritten character
  digits derived from the NIST Special Database 19  and converted to
  a 28x28 pixel image format and dataset structure that directly
  matches the MNIST dataset

  ~~~ Important note ~~~
  Please cite the following paper when using or referencing the dataset:
  Cohen, G., Afshar, S., Tapson, J., & van Schaik, A. (2017). EMNIST:
  an extension of MNIST to handwritten letters.
  Retrieved from http://arxiv.org/abs/1702.05373

"""

from tensorflow.keras.utils import get_file
from zipfile import ZipFile
from scipy import io as sio
import os
import logging


def warn_citation():
    """Warns about citation requirements
    # Returns
      Void
    """
    logging.warning(("Please cite the following paper when using or"
                     " referencing this Extra Keras Dataset:"))
    logging.warning(
        ("Cohen, G., Afshar, S., Tapson, J., & van Schaik, A. (2017). EMNIST: "
         "an extension of MNIST to handwritten letters. "
         "Retrieved from http://arxiv.org/abs/1702.05373")
      )


def load_data(path="emnist_matlab.npz", type="balanced"):
    """Loads the EMNIST dataset.
    # Arguments
        path: path where to cache the dataset locally
            (relative to ~/.keras/datasets).
        type: any of balanced, byclass, bymerge, digits, letters,
                mnist (defaults to balanced)
    # Returns
        Tuple of Numpy arrays: `(input_train, target_train),
                                  (input_test, target_test)`.
    """
    # Log about loading
    logging.basicConfig(level=logging.INFO)
    logging.info('Loading dataset = emnist')

    # Load data
    path = get_file(
        path, origin=("http://www.itl.nist.gov/iaui/vip/cs_links/EMNIST/"
                      "matlab.zip")
    )
    with ZipFile(path, "r") as opened_zip:

        # Read file and temporarily store it
        file_name = f"./{type}.mat"
        f = open(file_name, "wb")
        f.write(opened_zip.read(f"matlab/emnist-{type}.mat"))
        f.close()

        # Load data from Matlab file.
        # Source: https://stackoverflow.com/a/53547262
        mat = sio.loadmat(file_name)
        data = mat["dataset"]
        input_train = data["train"][0, 0]["images"][0, 0]
        target_train = data["train"][0, 0]["labels"][0, 0].flatten()
        input_test = data["test"][0, 0]["images"][0, 0]
        target_test = data["test"][0, 0]["labels"][0, 0].flatten()

        # Remove data when loaded
        os.remove(file_name)

        # Reshape input data
        # Source: https://stackoverflow.com/a/53547262
        input_train = input_train.reshape(
          (input_train.shape[0], 28, 28), order="F"
        )
        input_test = input_test.reshape(
          (input_test.shape[0], 28, 28), order="F"
        )

        # Warn about citation
        warn_citation()

        # Return data
        return (input_train, target_train), (input_test, target_test)
