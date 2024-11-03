# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from pyworld3 import World3
from pyworld3.utils import plot_world_variables
from matplotlib.pyplot import show

params = {'lines.linewidth': '3','axes.labelsize' : '12', 'xtick.labelsize' : '10', 'ytick.labelsize' : '10', 'figure.autolayout' : 'True'}
plt.rcParams.update(params)

"""
Referenze Run

Disclaimer: Szenario 2 and 3 do not match the szenarios of "Limits to Growth: The 30-year update", because some parameters were changed wich are not descriped.  
"""
world3 = World3(pyear = 4000)
world3.init_world3_constants(nri=2e12)
world3.init_world3_variables()
world3.set_world3_table_functions()
world3.set_world3_delay_functions()
world3.run_world3(fast=False)

plot_world_variables(world3.time,
                     [world3.nrfr, world3.io, world3.f, world3.pop,
                      world3.ppolx],
                     ["NRFR", "IO", "F", "POP", "PPOLX"],
                     [[0, 1.975], [0, 4e12], [0, 5.8e12], [0, 12e9], [0, 40]],
                     img_background="./img/fig 4-2-1.jpg",
                     figsize=(7, 5),
                     title="BAU2")
    
plot_world_variables(world3.time,
                     [world3.le, world3.fpc, world3.sopc, world3.ciopc],
                     ["LE", "FPC", "SOPC", "CIOPC"],
                     [[0, 90], [0,1000],[0,970], [0, 250]],
                     img_background="./img/fig 4-2-2.jpg",
                     figsize=(7, 5),
                     title="BAU2 - Material standard of living, 2004 Szenario 1")
    
    
plot_world_variables(world3.time,
                     [world3.ef, world3.hwi],
                     ["EF", "HWI"],
                     [[0, 4], [0,1]],
                     img_background="./img/fig 4-2-3.jpg",
                     figsize=(7, 5), title="BAU2 - Human Wellfare and Footprint, 2004 Szenario 1")
    
show()
