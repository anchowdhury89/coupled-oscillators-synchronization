# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
gp = Gnuplot.Gnuplot(persist = 1)
x = range(1000)
data = Gnuplot.Data(x, y, title='Plotting from Python')
gp('set data style lines')
gp('set xlabel "Label x"')
gp('set ylabel "Label y"')
gp.plot(data);
raw_input('Please press return to continue...\n')