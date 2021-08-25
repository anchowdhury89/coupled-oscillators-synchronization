# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
import random as random
b = -1
a = .5
k = 1
f = .355
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
def rx1f(x1,y1,t):
  return y1
def ry1f(x1,y1,t):
  g=w*t
  return -a*y1-b*x1-k*(x1**3)+f*cos(g)
h = 0.01
n = 10000
x=zeros((n,2))
x[0,0] = 0
x[0,1] = -.2
for i in range (0,n-1):
  k1x1 = rx1f(x[i,0],x[i,1],i*h)
  k1y1 = ry1f(x[i,0],x[i,1],i*h)
  k2x1 = rx1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,i*h+.5*h)
  k2y1 = ry1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,i*h+.5*h)
  k3x1 = rx1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,i*h+.5*h)
  k3y1 = ry1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,i*h+.5*h)
  k4x1 = rx1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,i*h+h)
  k4y1 = ry1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,i*h+h)
  x[i+1,0] = x[i,0] + h*(k1x1+2*k2x1+2*k3x1+k4x1)/6
  x[i+1,1] = x[i,1] + h*(k1y1+2*k2y1+2*k3y1+k4y1)/6
print x[n-1]
g = Gnuplot.Gnuplot()
g.title('Phase Space')
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
g.plot (x) 
h1.plot (x[:,0])
h2.plot (x[:,1])
plt = True
klo = float(raw_input('Do you want any more plots? 1/0 '))
if klo == 0: plt = False
while plt :
  m1 = float(raw_input('Range of Data Points(min) '))
  m2 = float(raw_input('Range of Data Points(max) '))
  xm = x[m1:m2,:] 
  g.plot (xm)
  h1.plot (x[(m1-1):(m2-1),0])
  h2.plot (x[(m1-1):(m2-1),1])
  g.hardcopy('Phase Space.ps', enhanced=1, color=1)
  h1.hardcopy('x.ps', enhanced=1, color=1)
  h2.hardcopy('y,ps', enhanced=1, color=1)
  klo = float(raw_input('Do you want any more plots? 1/0 '))
  if klo == 0:
    plt = False