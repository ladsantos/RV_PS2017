# Example Keplerian fit configuration file

# Required packages for setup
import os
import pandas as pd
import numpy as np
import radvel

# Define global planetary system and dataset parameters
starname = 'HD38529'
nplanets = 2    # number of planets in the system
instnames = ['het', 'keck', 'hjs', 'lick']    # list of instrument names. Can be whatever you like but should match 'tel' column in the input file.
ntels = len(instnames)       # number of instruments with unique velocity zero-points
fitting_basis = 'per tc secosw sesinw logk'    # Fitting basis, see radvel.basis.BASIS_NAMES for available basis names
bjd0 = 0   # reference epoch for RV timestamps (i.e. this number has been subtracted off your timestamps)
planet_letters = {1: 'b', 2: 'c'}   # map the numbers in the RVParameters keys to planet letters (for plotting and tables)

# Define prior centers (initial guesses) here.
params = radvel.RVParameters(nplanets,basis='per tp e w k', planet_letters=planet_letters)    # initialize RVparameters object

params['per1'] = 14.3104      # period of 1st planet
params['tp1'] = 2450020.19     # time of inferior conjunction of 1st planet
params['e1'] = 0.248          # eccentricity of 1st planet
params['w1'] = np.pi/2      # argument of periastron of the star's orbit for 1st planet
params['k1'] = 2.0          # velocity semi-amplitude for 1st planet
params['per2'] = 2134.76      # same parameters for 2nd planet ...
params['tp2'] = 2448002.0
params['e2'] = 0.36
params['w2'] = np.pi/6
params['k2'] = 3.3

time_base = 2453000          # abscissa for slope and curvature terms (should be near mid-point of time baseline)
params['dvdt'] = 0.0         # slope: (If rv is m/s and time is days then [dvdt] is m/s/day)
params['curv'] = 0.0         # curvature: (If rv is m/s and time is days then [curv] is m/s/day^2)

params['gamma_het'] = 0      # velocity zero-point for harps
params['gamma_keck'] = 0
params['gamma_hjs'] = 0
params['gamma_lick'] = 0

params['jit_het'] = 0.1      # velocity zero-point for harps
params['jit_keck'] = 0.1
params['jit_hjs'] = 0.1
params['jit_lick'] = 0.1

# Load radial velocity data, in this example the data is contained in
# an ASCII file, must have 'time', 'mnvel', 'errvel', and 'tel' keys
# the velocities are expected to be in m/s
data = pd.read_csv('../data/HD38529.dat', sep=',')

# Set parameters to vary (False means "hold constant"; default is for all parameters to vary).
#   Must be defined in the fitting basis
vary = dict(
    #per1=False,
    #per2=False,
    #secosw1=False,
    #secosw2=False,
    #sesinw1=False,
    #sesinw2=False,
    #logk1=False,
    #logk2=False,
    dvdt = False,
    curv = False,
    jit_het = True,
    jit_keck = True,
    jit_hjs = True,
    jit_lick = True
)


# Define prior shapes and widths here.
priors = [
    radvel.prior.EccentricityPrior( nplanets ),           # Keeps eccentricity < 1
    #radvel.prior.Gaussian('tc1', params['tc1'], 10.0),
    #radvel.prior.Gaussian('tc2', params['tc2'], 100.0),
    #radvel.prior.HardBounds('per1', 0, 2.0),
    #radvel.prior.HardBounds('per2', 100, 300.0),
    #radvel.prior.HardBounds('jit_harps', 0.0, 1.0)
]


# optional argument that can contain stellar mass in solar units (mstar) and
# uncertainty (mstar_err). If not set, mstar will be set to nan.
stellar = dict(mstar=1.48, mstar_err=0.05)
