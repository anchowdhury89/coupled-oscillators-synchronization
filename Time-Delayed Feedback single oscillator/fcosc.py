# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
import random as random
b = -1
a = .5
k = 1
f = .43
w = 1
c = 0.06
dl1 = 0.04
dl2 = 0.04
delay = 0.6
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
def rx1f(x1,y1,x1t,y1t,t):
  return y1
def ry1f(x1,y1,x1t,y1t,t):
  g=w*t
  return -a*y1-b*x1-k*(x1**3)+f*cos(g)+dl1*x1t+dl2*y1t
h = 0.1
n = 10000
ni = int(delay/h)
print ni
x = zeros((n,2))
for i in range (0,ni):
  x[i,0] = random.uniform(-1.5,-0.1)
  x[i,1] = random.uniform(-0.8,0.8)
for i in range (ni-1,n-1):
  k1x1 = rx1f(x[i,0],x[i,1],x[i-ni,0],x[i-ni,1],i*h)
  k1y1 = ry1f(x[i,0],x[i,1],x[i-ni,0],x[i-ni,1],i*h)
  k2x1 = rx1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i-ni,0]+.5*h*k1x1,x[i-ni,1]+.5*h*k1y1,i*h+.5*h)
  k2y1 = ry1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i-ni,0]+.5*h*k1x1,x[i-ni,1]+.5*h*k1y1,i*h+.5*h)
  k3x1 = rx1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i-ni,0]+.5*h*k2x1,x[i-ni,1]+.5*h*k2y1,i*h+.5*h)
  k3y1 = ry1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i-ni,0]+.5*h*k2x1,x[i-ni,1]+.5*h*k2y1,i*h+.5*h)
  k4x1 = rx1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i-ni,0]+h*k3x1,x[i-ni,1]+h*k3y1,i*h+h)
  k4y1 = ry1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i-ni,0]+h*k3x1,x[i-ni,1]+h*k3y1,i*h+h)
  x[i+1,0] = x[i,0] + h*(k1x1+2*k2x1+2*k3x1+k4x1)/6
  x[i+1,1] = x[i,1] + h*(k1y1+2*k2y1+2*k3y1+k4y1)/6
print x[n-1]
a = x[:,0:2]
g = Gnuplot.Gnuplot()
g.title('Phase Space a = .5, b = -1, k = 1, w = 1, f = .37, c=0.034')
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
h2.xlabel('t')
h2.ylabel('y')
g.plot (a) 
h1.plot (x[:,0])
plt = True
klo = float(raw_input('Do you want any more plots? 1/0 '))
if klo == 0: plt = False
while plt :
  m = float(raw_input('Enter no. of data points to be plotted '))
  am = a[(n-m):n,:]
  g.plot (am)
  h1.plot (x[(n-m):n,0])
  klo = float(raw_input('Do you want any more plots? 1/0 '))
  if klo == 0:
    plt = False