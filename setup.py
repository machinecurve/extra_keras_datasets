from setuptools import setup

setup(
    name="extra_keras_datasets",
    packages=["extra_keras_datasets"],
    version="{{VERSION}}",
    license="MIT",
    description="Extending the Keras Datasets module with extra ones.",
    long_description="Extending the Keras Datasets module with extra ones.",
    author="Christian Versloot",
    author_email="chris@machinecurve.com",
    url="https://github.com/christianversloot/extra_keras_datasets",
    download_url=("https://github.com/christianversloot/"
                  "extra_keras_datasets/archive/{{VERSION}}.tar.gz"),
    keywords=["keras", "datasets", "machine learning"],
    install_requires=["numpy", "scipy", "pandas", "scikit-learn"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
