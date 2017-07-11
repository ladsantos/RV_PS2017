# RV_PS2017

Jupyter Notebooks for the **radial velocities** tutorials at the Precision Spectroscopy Workshop 2017, held at the *Instituto de Astronomia, Geofísica e Ciências Atmosféricas* (*Universidade de São Paulo*) in August 2017.

Summary of this README:
1. Requirements
2. Setup
3. Technical background

### 1. Requirements

In order to follow this tutorial, it is necessary to have basic knowledge of command line in Unix-based systems. Having experience with Jupyter notebooks (a.k.a. IPython notebooks) and knowing how to use ``git`` and ``conda`` is recommended. The Python packages ``pandas``, ``radvel`` and ``radial`` (and their dependencies) need to be installed (see item 2). Basic knowledge of radial velocities and orbital parameters is also recommended (see item 3).

### 2. Setup

We highly recommend using the [Anaconda](https://www.continuum.io/downloads) ecosystem, since it allows us to use the ``conda`` Python package and environment manager. Additionally, we recommend downloading the Python 3 version of Anaconda -- but do not worry about Python 2 codes, because we can easily setup a Python 2 environment using ``conda``.

**Important note**: If you are a Linux user, you may run into problems when installing Python packages that compile C code with Anaconda. If the installation of the packages ``jupyter`` or ``radvel`` fails, use the following command to fix it:
```
conda install -c asmeurer gcc=4.8.5
```

For the radial velocities tutorials, we will create a Python 2.7 environment called ``rv``, and install the packages ``numpy``, ``scipy``, ``cython``, ``astropy``, ``pandas`` and ``matplotlib`` right from the start:

```
conda create -n rv python=2.7 numpy scipy cython astropy matplotlib pandas
```

Whenever you want to work in the ``rv`` environment, just issue the following command in the terminal:

```
source activate rv
```

And when you want to leave the environment, just use the following command:

```
source deactivate
```

Now, let's activate the ``rv`` environment and install some additional packages using the command ``pip``:

```
source activate rv
pip install emcee corner lmfit pp radvel jupyter
```

[``radvel``](http://radvel.readthedocs.io/en/master/index.html) is one of the radial velocities packages we will use in this tutorial. It is authored by B. J. Fulton and E. Petigura. Unfortunately it works only in Python 2, which is why we setup the ``rv`` environment with ``python=2.7``. The other package we will use in this tutorial is [``radial``](https://github.com/RogueAstro/radial), which is authored by L. dos Santos (it works in both Python 2 and 3, but it's optimized for Python 3).

In order to install ``radial``, go to the terminal and navigate to the folder you want to save the source code and issue the commands:

```
git clone https://github.com/RogueAstro/radial.git
cd radial
python setup.py develop
```

### 3. Technical background

The basic notions of radial velocities for binary stars and exoplanets can be found in chapter 2 of the book [Exoplanets by Sara Seager](http://seagerexoplanets.mit.edu/books.htm). This chapter is authored by C. D. Murray and A. C. M. Correia, and it is freely [available on arXiv](http://arxiv.org/abs/1009.1738).

Further reading for the enthusiasts:
* Minimum masses from minimal RV variation: [Torres (1999)](http://iopscience.iop.org/article/10.1086/316313), [Feng et al. (2015)](http://stacks.iop.org/0004-637X/800/i=1/a=22?key=crossref.07b640baf68c8ce0b4ded8aef8aa6074), [Jenkins et al. (2015)](http://arxiv.org/abs/1507.04749)
* Alpha Cen Bb does not exist: [Rajpaul et al. (2015)](http://arxiv.org/abs/1510.05598)
* The radial velocity fitting challenge: [Dumusque (2016)](http://arxiv.org/abs/1607.06487)
* Systemic Console: [Meschiari et al. (2009)](https://arxiv.org/abs/0907.1675)
* EXOFAST: [Eastman et al. (2013)](https://arxiv.org/abs/1206.5798)
* Markov Chain Monte Carlo techniques: [Ford (2005)](http://stacks.iop.org/1538-3881/129/i=3/a=1706)
* [Basic ``emcee`` example](http://dan.iel.fm/emcee/current/user/line/)
* [Fitting a plane to data](http://dan.iel.fm/posts/fitting-a-plane/)
* [A practical guide to the Lomb-Scargle Periodogram](http://jakevdp.github.io/blog/2017/03/30/practical-lomb-scargle/)
* [Frequentism vs. Bayesianism](http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/) (SPOILER: Frequentism sucks)
* [Toolkit for planet detection and characterization](https://reddots.space/toolkit/)
