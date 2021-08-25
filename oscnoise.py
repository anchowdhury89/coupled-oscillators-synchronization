# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
k1 = -1
b1 = .5
k3 = 1
a = 0
w = 1
def cos(x):
  if x != 0:
    xa = abs(x)
    sa = x/xa
    pi = 3.14159265359
    xm = xa%(2*pi)
    x = sa*xm
  err = 9999
  n = 2
  y = 1
  m = 1
  while err > 0.00000001:
    yprev = y
    m = m*n*(n-1)
    y = y + (((-1)**(n/2))*x**n)/m
    n = n + 2
    err = abs(y-yprev)
  return y
def rxf(x,y,t):
  return y
def ryf(x,y,t):
  g = w*t
  return -b1*y-k1*x-k3*(x**3)-a*cos(g)
h = 0.001
n = 30000
x = zeros((n,2))
x[0,0]=1
x[0,1]=1
for i in range (0,n-1):
  k1x = rxf(x[i,0],x[i,1],i+h)
  k1y = ryf(x[i,0],x[i,1],i*h)
  k2x = rxf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y,i*h+.5*h)
  k2y = ryf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y,i*h+.5*h)
  k3x = rxf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y,i*h+.5*h)
  k3y = ryf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y,i*h+.5*h)
  k4x = rxf(x[i,0]+h*k3x,x[i,1]+h*k3y,i*h+h)
  k4y = ryf(x[i,0]+h*k3x,x[i,1]+h*k3y,i*h+h)
  x[i+1,0] = x[i,0] + h*(k1x+2*k2x+2*k3x+k4x)/6
  x[i+1,1] = x[i,1] + h*(k1y+2*k2y+2*k3y+k4y)/6
print x[n-1]
g = Gnuplot.Gnuplot()
g.title('Nano1')
g.xlabel('x')
g.ylabel('y')
g('set data style lines')
h1 = Gnuplot.Gnuplot()
h2 = Gnuplot.Gnuplot()
h1.title('Time Series')
h1.xlabel('t')
h1.ylabel('x')
h1('set data style lines')
h2('set data style lines')
h2.title('Time Series')
h2.xlabel('t')
h2.ylabel('y')
g.plot (x) 
h1.plot(x[:,0])
h2.plot(x[:,1])
plt = True
klo = float(raw_input('Do you want any more plots? 1/0 '))
if klo == 0: plt = False
while plt :
  m = float(raw_input('Enter no. of data points to be plotted '))
  xm = x[(n-m):n,:]
  g.plot(xm)
  h1.plot(x[(n-m):n,0])
  h2.plot(x[(n-m):n,1])
  klo = float(raw_input('Do you want any more plots? 1/0 '))
  if klo == 0: plt = False