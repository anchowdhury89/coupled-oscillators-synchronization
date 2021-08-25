# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
k1 = 2
b1 = .05
k3 = 2
b3 = .3
m = 1
c = 2
def rxf(x,y):
  return y
def ryf(x,y):
  return -2*b1*y/m-k1*x-b3*(y**3)-k3*(x**3)
h = 0.001
n = 30000
x = zeros((n,2))
x[0,0]=.04
x[0,1]=.02
for i in range (0,n-1):
  k1x = rxf(x[i,0],x[i,1])
  k1y = ryf(x[i,0],x[i,1])
  k2x = rxf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y)
  k2y = ryf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y)
  k3x = rxf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y)
  k3y = ryf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y)
  k4x = rxf(x[i,0]+h*k3x,x[i,1]+h*k3y)
  k4y = ryf(x[i,0]+h*k3x,x[i,1]+h*k3y)
  x[i+1,0] = x[i,0] + h*(k1x+2*k2x+2*k3x+k4x)/6
  x[i+1,1] = x[i,1] + h*(k1y+2*k2y+2*k3y+k4y)/6
print x[n-1]
g = Gnuplot.Gnuplot(persist=1)
g.title('Nano1')
g.xlabel('x')
g.ylabel('y')
g('set data style lines')
g.plot (x) 
plt = True
klo = float(raw_input('Do you want any more plots? 1/0 '))
if klo == 0: plt = False
while plt :
  m = float(raw_input('Enter no. of data points to be plotted '))
  xm = x[(n-m):n,:]
  g.plot (xm)
  klo = float(raw_input('Do you want any more plots? 1/0 '))
  if klo == 0:
    plt = False
