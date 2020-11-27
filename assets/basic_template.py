'''
  Import the <Dataset name>
  Source: <URL to dataset>
  Description: <Short dataset description>

  ~~~ Important note ~~~
  Please cite the following work when using or referencing the dataset:
  <Citation>

'''

from tensorflow.keras.utils import get_file
import numpy as np

def load_data(path='<Dataset_slug>.npz', size='small'):
  """Loads the <Dataset name>
  # Arguments
      path: path where to cache the dataset locally
          (relative to ~/.keras/datasets).
      size: small or large, indicating dummy dataset size to return.
  # Returns
      Tuple of Numpy arrays: `(input_train, target_train), (input_test, target_test)`.
  """

    if size == 'small':
      input_train = np.array([1, 2])
      target_train = np.array([0, 1])
      input_test = np.array([2, 3])
      target_test = np.array([1, 0])
    else:
      input_train = np.array([1, 2, 84, 9, 1, 48, 2])
      target_train = np.array([0, 1, 0, 0, 0, 1, 1])
      input_test = np.array([2, 3, 32, 84, 99, 1, 2])
      target_test = np.array([1, 0, 0, 0, 1, 0, 1])
  
    return (input_train, target_train), (input_test, target_test)