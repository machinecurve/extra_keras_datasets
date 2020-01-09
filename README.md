<p align="center">
  <img src="assets/extra_k_logo_neg.png" width="300" style="border: 3px solid #f6f8fa;">
</p>

Hi there, and welcome to the `extra-keras-datasets` module! This extension to the original `keras.datasets` module offers easy access to additional datasets, in ways almost equal to how you're currently importing them.

**Powered by MachineCurve at www.machinecurve.com**

## Table of Contents
- [Table of Contents](#table-of-contents)
- [How to use this module?](#how-to-use-this-module-)
  * [Dependencies](#dependencies)
  * [Installation procedure](#installation-procedure)
- [Datasets](#datasets)
  * [EMNIST-Balanced](#emnist-balanced)
  * [EMNIST-ByClass](#emnist-byclass)
  * [EMNIST-ByMerge](#emnist-bymerge)
  * [EMNIST-Digits](#emnist-digits)
  * [EMNIST-Letters](#emnist-letters)
  * [EMNIST-MNIST](#emnist-mnist)
  * [KMNIST-KMNIST](#kmnist-kmnist)
  * [KMNIST-K49](#kmnist-k49)
  * [SVHN-Normal](#svhn-normal)
  * [SVHN-Extra](#svhn-extra)
- [Contributors and other references](#contributors-and-other-references)
- [License](#license)

## How to use this module?
### Dependencies
TODO.

### Installation procedure
Installing is really easy, and can be done with [PIP](https://pypi.org/project/extra-keras-datasets/): `pip install extra-keras-datasets`.

## Datasets

### EMNIST-Balanced
Extended MNIST (EMNIST) contains digits as well as uppercase and lowercase handwritten letters. `EMNIST-Balanced` contains 131.600 characters across 47 balanced classes.

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='balanced')
```

<a href="./assets/emnist-balanced.png"><img src="./assets/emnist-balanced.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-ByClass
Extended MNIST (EMNIST) contains digits as well as uppercase and lowercase handwritten letters. `EMNIST-ByClass` contains 814.255 characters across 62 unbalanced classes.

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='byclass')
```

<a href="./assets/emnist-byclass.png"><img src="./assets/emnist-byclass.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-ByMerge
Extended MNIST (EMNIST) contains digits as well as uppercase and lowercase handwritten letters. `EMNIST-ByMerge` contains 814.255 characters across 47 unbalanced classes.

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='bymerge')
```

<a href="./assets/emnist-bymerge.png"><img src="./assets/emnist-bymerge.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-Digits
Extended MNIST (EMNIST) contains digits as well as uppercase and lowercase handwritten letters. `EMNIST-Digits` contains 280.000 characters across 10 balanced classes (digits only).

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='digits')
```

<a href="./assets/emnist-digits.png"><img src="./assets/emnist-digits.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-Letters
Extended MNIST (EMNIST) contains digits as well as uppercase and lowercase handwritten letters. `EMNIST-Letters` contains 145.600 characters across 26 balanced classes (letters only).

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='letters')
```

<a href="./assets/emnist-letters.png"><img src="./assets/emnist-letters.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-MNIST
Extended MNIST (EMNIST) contains digits as well as uppercase and lowercase handwritten letters. `EMNIST-MNIST` contains 70.000 characters across 10 balanced classes (equal to `keras.datasets.mnist`).

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='mnist')
```

<a href="./assets/emnist-mnist.png"><img src="./assets/emnist-mnist.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### KMNIST-KMNIST
Kuzushiji-MNIST is a drop-in replacement for the MNIST dataset: it contains 70.000 28x28 grayscale images of Japanese Kuzushiji characters.

```
from extra-keras-datasets import kmnist
(input_train, target_train), (input_test, target_test) = kmnist.load_data(type='kmnist')
```

<a href="./assets/kmnist-kmnist.png"><img src="./assets/kmnist-kmnist.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### KMNIST-K49
Kuzushiji-49 extends Kuzushiji-MNIST and contains 270.912 images across 49 classes.

```
from extra-keras-datasets import kmnist
(input_train, target_train), (input_test, target_test) = kmnist.load_data(type='k49')
```

<a href="./assets/kmnist-k49.png"><img src="./assets/kmnist-k49.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### SVHN-Normal
The Street View House Numbers dataset (SVHN) contains 32x32 cropped images of house numbers obtained from Google Street View. There are 73.257 digits for training and 26.032 digits for testing. **Noncommercial** use is allowed only: [see the SVHN website for more information](http://ufldl.stanford.edu/housenumbers/).

```
from extra-keras-datasets import svhn
(input_train, target_train), (input_test, target_test) = svhn.load_data(type='normal')
```

<a href="./assets/svhn-normal.png"><img src="./assets/svhn-normal.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### SVHN-Extra
SVHN-Extra extends SVHN-Normal with 531.131 less difficult samples and contains a total of 604.388 digits for training and 26.032 digits for testing. **Noncommercial** use is allowed only: [see the SVHN website for more information](http://ufldl.stanford.edu/housenumbers/).

```
from extra-keras-datasets import svhn
(input_train, target_train), (input_test, target_test) = svhn.load_data(type='extra')
```

<a href="./assets/svhn-extra.png"><img src="./assets/svhn-extra.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

## Contributors and other references
* **EMNIST dataset:**
  * Cohen, G., Afshar, S., Tapson, J., & van Schaik, A. (2017). EMNIST: an extension of MNIST to handwritten letters. Retrieved from http://arxiv.org/abs/1702.05373
  * [tlindbloom](https://stackoverflow.com/users/4008755/tlindbloom) on StackOverflow: [loading EMNIST-letters dataset](https://stackoverflow.com/questions/51125969/loading-emnist-letters-dataset/53547262#53547262) in [emnist.py](./emnist.py).
* **KMNIST dataset:**
  * Clanuwat, T., Bober-Irizar, M., Kitamoto, A., Lamb, A., Yamamoto, K., & Ha, D. (2018). Deep learning for classical Japanese literature. arXiv preprint arXiv:1812.01718. Retrieved from https://arxiv.org/abs/1812.01718
* **SVHN dataset:**
  * Netzer, Y., Wang, T., Coates, A., Bissacco, A., Wu, B., & Ng, A. Y. (2011). Reading digits in natural images with unsupervised feature learning. Retrieved from http://ufldl.stanford.edu/housenumbers/nips2011_housenumbers.pdf / http://ufldl.stanford.edu/housenumbers/

## License
The licenseable parts of this repository are licensed under a [MIT License](./LICENSE), so you're free to use this repo in your machine learning projects / blogs / exercises, and so on. Happy engineering! 🚀