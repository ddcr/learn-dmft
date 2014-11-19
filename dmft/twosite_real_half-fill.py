# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 15:12:44 2014

@author: oscar
"""

from __future__ import division, absolute_import, print_function
import matplotlib.pyplot as plt
import numpy as np
from twosite import twosite, out_plot

if __name__ == "__main__":
    res = []
    for U in np.arange(0, 4, 0.2):

        sim = twosite(80, 0.5, 'real')
        hyb = 0.5  # np.sqrt(sim.imp_z()*sim.m2)
        fig = plt.figure()
        for i in range(80):
            old = hyb
            hyb = sim.solve(U/2, U/2, U, old)
            out_plot(sim, 'A', 'loop {} hyb {}'.format(i, hyb))
            if np.abs(old - hyb) < 1e-6:
                break

        plt.legend()
        plt.title('U={}, hyb={}'.format(U, hyb))
        plt.ylabel('A($\omega$)')
        plt.xlabel('$\omega$')
        fig.savefig('Aw_halffill_{:.2f}.png'.format(U), format='png',
                    transparent=False, bbox_inches='tight', pad_inches=0.05)
        plt.close(fig)
        res.append((U, sim))
    np.save('realax_halffill', res)
