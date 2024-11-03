# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import json
from pyworld3 import World3
from pyworld3.utils import plot_world_variables
from matplotlib.pyplot import show

params = {'lines.linewidth': '3','axes.labelsize' : '12', 'xtick.labelsize' : '10', 'ytick.labelsize' : '10', 'figure.autolayout' : 'True'}
plt.rcParams.update(params)

"""
Read constants from a file
"""

# The 'constants.json' are modified for "recalibration23"
# https://onlinelibrary.wiley.com/doi/full/10.1111/jiec.13442
with open('constants.json', 'r') as file:
    data = json.load(file)
params = dict()
for k in iter(data['constants']):
    params[k] = data['constants'][k]['value']
    
world3 = World3(pyear = 4000)
world3.init_world3_constants(**params)
world3.init_world3_variables()
world3.set_world3_table_functions()
world3.set_world3_delay_functions()
world3.run_world3(fast=False)

plot_world_variables(world3.time,
                     [world3.nrfr, world3.io, world3.f, world3.pop,
                      world3.ppolx],
                     ["NRFR", "IO", "F", "POP", "PPOLX"],
                     [[0, 1.975], [0, 4e12], [0, 5.8e12], [0, 12e9], [0, 40]],
                     figsize=(7, 5),
                     title="BAU2")
    
plot_world_variables(world3.time,
                     [world3.le, world3.fpc, world3.sopc, world3.ciopc],
                     ["LE", "FPC", "SOPC", "CIOPC"],
                     [[0, 90], [0,1000],[0,970], [0, 250]],
                     figsize=(7, 5),
                     title="BAU2 - Material standard of living, 2004 Szenario 1")
    
    
plot_world_variables(world3.time,
                     [world3.ef, world3.hwi],
                     ["EF", "HWI"],
                     [[0, 4], [0,1]],
                     figsize=(7, 5), title="BAU2 - Human Wellfare and Footprint, 2004 Szenario 1")
    
show()
