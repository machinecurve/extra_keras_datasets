"""
  Import the USPS Handwritten Digits Dataset
  Source: https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/
          multiclass.html#usps
  (and: https://ieeexplore.ieee.org/document/291440)
  Description: Handwritten text recognition image database.

  ~~~ Important note ~~~
  Please cite the following paper when using or referencing the dataset:
  Hull, J. J. (1994). A database for handwritten text recognition
  research. IEEE Transactions on pattern analysis and machine
  intelligence, 16(5), 550-554.
"""

from tensorflow.keras.utils import get_file
import logging
from sklearn.datasets import load_svmlight_file
import bz2


def warn_citation():
    """Warns about citation requirements
    # Returns
      Void
    """
    logging.warning(("Please cite the following paper when using or"
                     " referencing this Extra Keras Dataset:"))
    logging.warning(
        ("Hull, J. J. (1994). A database for handwritten text "
         "recognition research. IEEE Transactions on pattern analysis and "
         "machine intelligence, 16(5), 550-554.")
      )


def decompress(path):
    """Decompresses BZ2 data into another file"""
    bz_zip = bz2.BZ2File(path)
    decompressed_data = bz_zip.read()
    new_path = path[:-4]
    open(new_path, 'wb').write(decompressed_data)
    return new_path


def load_to_numpy(path):
    """Loads LIBSVM data into NumPY format"""
    data = load_svmlight_file(path)
    return (data[0].toarray(), data[1])


def load_data(
    path="usps.bz2",
    path_testing="usps-testing.bz2"
):
    """Loads the USPS Handwritten Digits Dataset.
    # Arguments
        path: path where to cache the USPS data locally
            (relative to ~/.keras/datasets).
        path_testing: path where to cache the USPS testing data locally
            (relative to ~/.keras/datasets).
    # Returns
        Tuple of Numpy arrays: `(input_train, target_train),
                                  (input_test, target_test)`.
        Input structure: 16x16 image with a digit
        Target structure: number in the 0.0 - 9.0 range

    """
    # Log about loading
    logging.basicConfig(level=logging.INFO)
    logging.info('Loading dataset = usps')

    # Download data
    path = get_file(
        path,
        origin=("https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/"
                "datasets/multiclass/usps.bz2")
    )
    path_testing = get_file(
        path_testing,
        origin=("https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/"
                "datasets/multiclass/usps.t.bz2")
    )

    # Decompress data
    decompress_train = decompress(path)
    decompress_test = decompress(path_testing)

    # Load LIBSVM data into NumPy array
    (input_train, target_train) = load_to_numpy(decompress_train)
    (input_test, target_test) = load_to_numpy(decompress_test)

    # Reshape data
    input_train = input_train.reshape(input_train.shape[0], 16, 16)
    input_test = input_test.reshape(input_test.shape[0], 16, 16)

    # Correct targets (e.g. number 3 is now returned as 4.0)
    target_train = target_train - 1
    target_test = target_test - 1

    # Warn about citation
    warn_citation()

    # Return data
    return (input_train, target_train), (input_test, target_test)
