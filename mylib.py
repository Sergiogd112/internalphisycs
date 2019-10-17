import astropy
import astroplan
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os
import time
import pickle as pk
from time import gmtime
from astropy.coordinates import solar_system_ephemeris
from astropy.time import Time as tm
from astropy.coordinates import EarthLocation as eloc
from astroplan import Observer


def println(n):
    print('_' * n)


def moonin(time, obs):
    rise = obs.moon_rise_time(time=time)
    set = obs.moon_set_time(time=time)
    if(rise >= set):
        state = False
    else:
        state = True
    return state


def getepoch(name, path):
    fname = name[(len(path)):]
    epoch = tm(float(fname[len('imegen_'):(
        len('imagen_') + len('1566201613'))]), format='unix')
    return epoch


def move(old, new):
    os.system('sudo mv ' + old + ' ' + new)


def overexposed(path, maxavg):
    im = plt.imread(path)
    print(np.average(im))


def main(arr):
    fname, ln, deldir, basedir, obs = arr
    epoch = getepoch(fname, basedir)
    print(epoch)
    if(not(moonin(epoch, obs))):
        println(ln)
        print('out')
        print(fname, deldir + fname[len(basedir):])
        println(ln)
        move(fname, deldir + fname[len(basedir):])
    else:
        println(ln)
        print('in')
        print(fname)
        println(ln)
