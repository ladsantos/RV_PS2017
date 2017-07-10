# RV_PS2017

Jupyter Notebooks for the **radial velocities** tutorials at the Precision Spectroscopy Workshop 2017, held at the Instituto de Astronomia, Geofísica e Ciências Atmosféricas (Universidade de São Paulo) in August 2017.

Requirements
------------

In order to follow this tutorial, it is necessary to have basic knowledge of command line in Unix-based systems. Knowing how to use ``git`` is recommended. The Python packages ``pandas``, ``radvel`` and ``radial`` (and their dependencies) need to be installed (see below for instructions).

Setup
-----

We highly recommend using the [Anaconda](https://www.continuum.io/downloads) ecosystem, since it allows us to use the ``conda`` Python package and environment manager. Additionally, we recommend downloading the Python 3 version of Anaconda -- but do not worry about Python 2 codes, because we can easily setup a Python 2 environment using ``conda``.

**Important note**: If you are a Linux user, you may run into problems when installing Python packages that compile C code with Anaconda. If the installation of the packages ``jupyter`` or ``radvel`` fails, use the following command to fix it:
```
$ conda install -c asmeurer gcc=4.8.5
```

For the radial velocities tutorials, we will create a Python 2.7 environment called ``rv``, and install the packages ``numpy``, ``scipy``, ``cython``, ``astropy``, ``pandas`` and ``matplotlib`` right from the start:

```
$ conda create -n rv python=2.7 numpy scipy cython astropy matplotlib pandas
```

Whenever you want to work in the ``rv`` environment, just issue the following command in the terminal:

```
$ source activate rv
```

And when you want to leave the environment, just use the following command:

```
$ source deactivate
```

Now, let's activate the ``rv`` environment and install some additional packages using the command ``pip``:

```
$ source activate rv
$ pip install emcee corner lmfit pp radvel jupyter
```

[``radvel``](http://radvel.readthedocs.io/en/master/index.html) is one of the radial velocities packages we will use in this tutorial. It is authored by B. J. Fulton and E. Petigura. Unfortunately it works only in Python 2, which is why we setup the ``rv`` environment with ``python=2.7``. The other package we will use in this tutorial is [``radial``](https://github.com/RogueAstro/radial), which is authored by L. dos Santos (it works in both Python 2 and 3, but it's optimized for Python 3).

In order to install ``radial``, got to the terminal and navigate to the folder you want to save the source code and issue the command:

```
$ git clone https://github.com/RogueAstro/radial.git
$ cd radial
$ python setup.py install
```
