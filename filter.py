import astropy
import astroplan
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os

ln = 30


def println(n):
    print('_' * n)


basedir = 'Analema/'
photopath = [basedir + x for x in os.listdir(basedir)]

println(ln)
print(photopath[:10])
println(ln)
