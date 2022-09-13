from random import gauss
import matplotlib.pyplot as mpl
import numpy as np
from gauss import Gauss
from algorytm import mrq


if __name__ == '__main__':

    y = []
    x = []
    p = []
    sig = []
    f = open("ELABLP.DAT", 'r')
    for ind, dat in enumerate(f):
        dat = dat.split(' ')
        if ind > 0:
            x.append(float(dat[2]))
            y.append(float(dat[3]))
            sig.append(1)
    f.close()
    f = open('PARLIP1.DAT', 'r')
    for ind, dat in enumerate(f):
        dat = dat.split(' ')
        if ind > 0:
            try:
                p.append(float(dat[-1]))
            except:
                pass
    f.close()
mpl.plot(x, y)
mpl.show()
