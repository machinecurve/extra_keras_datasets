from __future__ import absolute_import

__version__ = '{{VERSION}}'

from . import emnist
from . import kmnist
from . import svhn
from . import stl10
from . import iris
from . import wine_quality
from . import usps

__all__ = ['emnist', 'kmnist', 'svhn', 'stl10', 'iris', 'wine_quality', 'usps']
