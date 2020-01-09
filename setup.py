from distutils.core import setup
setup(
  name = 'extra_keras_datasets',
  packages = ['extra_keras_datasets'],
  version = '0.1.1',
  license='MIT',
  description = 'Extending the Keras Datasets module with extra ones.',
  author = 'Christian Versloot',
  author_email = 'chris@machinecurve.com',
  url = 'https://github.com/christianversloot/extra_keras_datasets',
  download_url = 'https://github.com/christianversloot/extra_keras_datasets/archive/0.1.1.tar.gz',
  keywords = ['keras', 'datasets', 'machine learning'],
  install_requires=[
    'keras',
    'numpy',
    'scipy'
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)