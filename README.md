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
- [Contributors and other references](#contributors-and-other-references)
- [License](#license)

## How to use this module?
### Dependencies
TODO.

### Installation procedure
Installing is really easy, and can be done with [PIP](https://pypi.org/project/extra-keras-datasets/): `pip install extra-keras-datasets`.

## Datasets

### EMNIST-Balanced

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='balanced')
```

<a href="./assets/emnist-balanced.png"><img src="./assets/emnist-balanced.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-ByClass

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='byclass')
```

<a href="./assets/emnist-byclass.png"><img src="./assets/emnist-byclass.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-ByMerge

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='bymerge')
```

<a href="./assets/emnist-bymerge.png"><img src="./assets/emnist-bymerge.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-Digits

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='digits')
```

<a href="./assets/emnist-digits.png"><img src="./assets/emnist-digits.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-Letters

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='letters')
```

<a href="./assets/emnist-letters.png"><img src="./assets/emnist-letters.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-MNIST

```
from extra-keras-datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='mnist')
```

<a href="./assets/emnist-mnist.png"><img src="./assets/emnist-mnist.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### KMNIST-KMNIST

```
from extra-keras-datasets import kmnist
(input_train, target_train), (input_test, target_test) = kmnist.load_data(type='kmnist')
```

<a href="./assets/kmnist-kmnist.png"><img src="./assets/kmnist-kmnist.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### KMNIST-K49

```
from extra-keras-datasets import kmnist
(input_train, target_train), (input_test, target_test) = kmnist.load_data(type='k49')
```

<a href="./assets/kmnist-k49.png"><img src="./assets/kmnist-k49.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

## Contributors and other references
* **EMNIST dataset:**
  * Cohen, G., Afshar, S., Tapson, J., & van Schaik, A. (2017). EMNIST: an extension of MNIST to handwritten letters. Retrieved from http://arxiv.org/abs/1702.05373
  * [tlindbloom](https://stackoverflow.com/users/4008755/tlindbloom) on StackOverflow: [loading EMNIST-letters dataset](https://stackoverflow.com/questions/51125969/loading-emnist-letters-dataset/53547262#53547262) in [emnist.py](./emnist.py).
* **KMNIST dataset:**
  * Clanuwat, T., Bober-Irizar, M., Kitamoto, A., Lamb, A., Yamamoto, K., & Ha, D. (2018). Deep learning for classical Japanese literature. arXiv preprint arXiv:1812.01718. Retrieved from https://arxiv.org/abs/1812.01718

## License
The licenseable parts of this repository are licensed under a [MIT License](./LICENSE), so you're free to use this repo in your machine learning projects / blogs / exercises, and so on. Happy engineering! 🚀