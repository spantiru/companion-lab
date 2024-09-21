[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/spantiru/companion-lab/master)

# JupyterLab for the Machine Learning seminar

Ștefan Panțiru, Faculty of Computer Science Iași

To run this lab, either click the `launch binder` button above, or run the code on your machine following the instructions below.

Useful resources:
* [ML Homework](https://forms.gle/EmPiJqABNR7MZWgf8)
* [Register for Piazza](https://forms.gle/KQP3pwRQxvqxVvLz6)
* [Resources uploaded to Piazza](https://piazza.com/info.uaic.ro/fall2023/ml2023f/resources)
* [Python official documentation](https://docs.python.org/3.12/library/index.html)
* [Scikit-learn library](https://scikit-learn.org/stable/getting_started.html) - machine learning library for Python
* [Scipy statistical functions](https://docs.scipy.org/doc/scipy/reference/stats.html)
* [Pandas library](https://pandas.pydata.org/docs/reference/index.html) - library providing data structures and analysis tools for Python

## Running locally

This lab uses Python 3.12 and `pipenv`, so make sure they are available on your system.

```bash
$ python3 --version
Python 3.12.3
$ python3 -m pipenv --version
pipenv, version 2023.12.1
```

Clone the repository using git:

```bash
$ git clone https://github.com/spantiru/companion-lab.git
```

Inside the project folder, create the pipenv environment:

```bash
$ cd companion-lab
$ python3 -m pipenv install # Might take a few seconds
```

Run `jupyter-lab`, which should start in your default browser:

```bash
$ python3 -m pipenv run jupyter-lab
```