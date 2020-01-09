'''
  Import the KMNIST dataset
  Source: https://arxiv.org/abs/1812.01718
  Description: Japanese character MNIST dataset.

  ~~~ Important note ~~~
  Please cite the following paper when using or referencing the dataset:
  Clanuwat, T., Bober-Irizar, M., Kitamoto, A., Lamb, A., Yamamoto, K., & Ha, D. (2018). Deep learning for classical Japanese literature. arXiv preprint arXiv:1812.01718. Retrieved from https://arxiv.org/abs/1812.01718

'''

from keras.utils.data_utils import get_file
import numpy as np

def load_data(path='kmnist.npz', type='kmnist'):
  """Loads the KMNIST dataset.
  # Arguments
      path: path where to cache the dataset locally
          (relative to ~/.keras/datasets).
      type: any of kmnist, k49
  # Returns
      Tuple of Numpy arrays: `(input_train, target_train), (input_test, target_test)`.
  """
  # Load training images
  path_train = get_file(
    f'{path}_{type}_train_imgs',
    origin=f'http://codh.rois.ac.jp/kmnist/dataset/{type}/{type}-train-imgs.npz'
  )
  input_train = np.load(path_train)['arr_0']

  # Load training labels
  path_train_labels = get_file(
    f'{path}_{type}_train_labels',
    origin=f'http://codh.rois.ac.jp/kmnist/dataset/{type}/{type}-train-labels.npz'
  )
  target_train = np.load(path_train_labels)['arr_0']

  # Load testing images
  path_test = get_file(
    f'{path}_{type}_test_imgs',
    origin=f'http://codh.rois.ac.jp/kmnist/dataset/{type}/{type}-test-imgs.npz'
  )
  input_test = np.load(path_test)['arr_0']

  # Load testing labels
  path_test_labels = get_file(
    f'{path}_{type}_test_labels',
    origin=f'http://codh.rois.ac.jp/kmnist/dataset/{type}/{type}-test-labels.npz'
  )
  target_test = np.load(path_test_labels)['arr_0']

  # Return data
  return (input_train, target_train), (input_test, target_test)
