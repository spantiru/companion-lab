[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/spantiru/companion-lab/master)

# JupyterLab for the Machine Learning seminar

Ștefan Panțiru, Faculty of Computer Science, "Alexandru Ioan Cuza" University Iași

To run this lab, either click the `launch binder` button above, or run the code on your machine following the instructions below.

## Contents
* [Lab01 - Elementary Notions in Probability and Statistics](Lab01.ipynb)
* [Lab02 - Decision Trees (part1)](Lab02.ipynb) 
* [Lab03 - Decision Trees (part2)](Lab03.ipynb)
* [Lab04 - Decision Trees (part3)](Lab04.ipynb)
* [Lab05 - Naive Bayes (part1)](Lab05.ipynb)
* [Lab06 - Naive Bayes (part2)](Lab06.ipynb)
* [Lab07 - Maximum Likelihood Estimation](Lab07.ipynb)
* Week 8 - Midterm Exam
* [Lab09 - Logistic Regression](Lab09.ipynb)
* [Lab10 - k-Nearest Neighbour](Lab10.ipynb)
* [Lab11 - AdaBoost](Lab11.ipynb)
* [Lab12 - Hierarchical Clustering](Lab12.ipynb)
* [Lab13 - k-Means (part1)](Lab13.ipynb)
* [Lab14 - k-Means (part2)](Lab14.ipynb)

## Useful resources:
* [ML Homework](https://forms.gle/EmPiJqABNR7MZWgf8)
* [Register for Piazza](https://forms.gle/KQP3pwRQxvqxVvLz6)
* [Resources uploaded to Piazza](https://piazza.com/info.uaic.ro/spring2024/ml2024f/resources)
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
