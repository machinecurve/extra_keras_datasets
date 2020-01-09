'''
  Import the STL-10 dataset
  Source: https://cs.stanford.edu/~acoates/stl10/
  Description: The STL-10 dataset is an image recognition dataset for developing unsupervised feature learning, deep learning, self-taught learning algorithms.

  ~~~ Important note ~~~
  Please cite the following paper when using or referencing the dataset:
  Coates, A., Ng, A., & Lee, H. (2011, June). An analysis of single-layer networks in unsupervised feature learning. In Proceedings of the fourteenth international conference on artificial intelligence and statistics (pp. 215-223). Retrieved from http://cs.stanford.edu/~acoates/papers/coatesleeng_aistats_2011.pdf

'''

from keras.utils.data_utils import get_file
from scipy import io as sio
import shutil
import numpy as np

def load_data(path='stl10_matlab.tar.gz'):
  """Loads the STL-10 dataset.
  # Arguments
      path: path where to cache the dataset locally
          (relative to ~/.keras/datasets).
  # Returns
      Tuple of Numpy arrays: `(input_train, target_train), (input_test, target_test)`.
  """
  path = get_file(path,
                    origin='http://ai.stanford.edu/~acoates/stl10/stl10_matlab.tar.gz')

  # Temporarily extract .tar.gz in local path
  local_targz_path = './stl-10'
  shutil.unpack_archive(path, local_targz_path)

  # Load data from Matlab file
  # Source: https://stackoverflow.com/a/53547262
  train = sio.loadmat(f'{local_targz_path}/stl10_matlab/train.mat', )
  test = sio.loadmat(f'{local_targz_path}/stl10_matlab/test.mat')

  # Remove temporary file
  shutil.rmtree(local_targz_path, ignore_errors=True)

  # Define training data
  input_train = train['X'].reshape((-1, 3, 96, 96))
  input_train = np.transpose(input_train, (0, 3, 2, 1))
  target_train = train['y'].flatten()

  # Define testing data
  input_test = test['X'].reshape((-1, 3, 96, 96))
  input_test = np.transpose(input_test, (0, 3, 2, 1))
  target_test = test['y'].flatten()

  # Return data
  return (input_train, target_train), (input_test, target_test)