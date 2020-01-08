<p align="center">
  <img src="assets/extra_k_logo_neg.png" width="300" style="border: 3px solid #f6f8fa;">
</p>

Hi there, and welcome to the `extra_keras_datasets` module! This extension to the original `keras.datasets` module offers easy access to additional datasets that can easily be integrated with your Keras models, in ways almost equal to how you're currently importing them.

**Powered by MachineCurve at www.machinecurve.com**

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Datasets](#datasets)
  * [EMNIST-Balanced](#emnist-balanced)
  * [EMNIST-ByClass](#emnist-byclass)
  * [EMNIST-ByMerge](#emnist-bymerge)
  * [EMNIST-Digits](#emnist-digits)
  * [EMNIST-Letters](#emnist-letters)
  * [EMNIST-MNIST](#emnist-mnist)
- [Contributors and other references](#contributors-and-other-references)
- [License](#license)

## Datasets

### EMNIST-Balanced

```
from extra_keras_datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='balanced')
```

<a href="./assets/emnist-balanced.png"><img src="./assets/emnist-balanced.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-ByClass

```
from extra_keras_datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='byclass')
```

<a href="./assets/emnist-byclass.png"><img src="./assets/emnist-byclass.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-ByMerge

```
from extra_keras_datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='bymerge')
```

<a href="./assets/emnist-bymerge.png"><img src="./assets/emnist-bymerge.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-Digits

```
from extra_keras_datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='digits')
```

<a href="./assets/emnist-digits.png"><img src="./assets/emnist-digits.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-Letters

```
from extra_keras_datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='letters')
```

<a href="./assets/emnist-letters.png"><img src="./assets/emnist-letters.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

### EMNIST-MNIST

```
from extra_keras_datasets import emnist
(input_train, target_train), (input_test, target_test) = emnist.load_data(type='mnist')
```

<a href="./assets/emnist-mnist.png"><img src="./assets/emnist-mnist.png" width="500" style="border: 3px solid #f6f8fa;" /></a>

---

## Contributors and other references
* **[tlindbloom](https://stackoverflow.com/users/4008755/tlindbloom) on StackOverflow:** [loading EMNIST-letters dataset](https://stackoverflow.com/questions/51125969/loading-emnist-letters-dataset/53547262#53547262) in [emnist.py](./emnist.py).

## License
The licenseable parts of this repository are licensed under a [MIT License](./LICENSE), so you're free to use this repo in your machine learning projects / blogs / exercises, and so on. Happy engineering! 🚀