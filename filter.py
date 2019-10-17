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
from mylib import *
from multiprocessing import Pool

ln = 30
t = tm(time.time(), format='unix')
location = eloc.from_geodetic(lon=41.385728, lat=2.055923)
basedir = 'Analema/'
deldir = 'delAnalema/'
obs = Observer(longitude=41.385728, latitude=2.055923)

rise = obs.moon_rise_time(time=t)
println(ln)
print(rise, rise.to_datetime())
println(ln)

photopath = [basedir + x for x in os.listdir(basedir)]

println(ln)
print(photopath[:10])
println(ln)
println(ln)
bigarr = [[x, ln, deldir, basedir, obs] for x in photopath]
pool = Pool(3)
pool.map(main, bigarr)
