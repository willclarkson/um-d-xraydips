import numpy as np
import os

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

from scipy.optimize import curve_fit

def mjd_to_phase (

    MJD_n,
    MJD_0 = 50082.04,
    P = 16.54694,
    P_0 = 3.53e-5
):
    MJD_n = np.atleast_1d(MJD_n).astype(float).ravel()
    
    delta = MJD_n - MJD_0
    #discriminant:
    discriminant = (P)**2 - 4*P_0*delta

    if np.any(discriminant < 0):
        raise ValueError("Discriminant is less than 0 (negative), so no real roots exist.")


    square_root = np.sqrt(discriminant)

    #two roots:
    N1 = (P - square_root)/(2*P_0)
    N2 = (P - square_root)/(2*P_0)
    bpos = N1 > 0
    N = np.copy(N2)
    N[bpos] = N1[bpos]

    #orbital phase:
    phase = N - np.floor(N)
    return phase
