# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
f0 = 123200
q = 720
k = 2
f = 173200
B = 0
m = 1
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
  ft = 46787*t
  return -f0*y/q-(f0**2)*x-k*(x**3)+B*cos(ft)
h = 0.001
n = 30000
x = zeros((n,2))
x[0,0]=.04
x[0,1]=.02
for i in range (0,n-1):
  k1x = rxf(x[i,0],x[i,1],n*h)
  k1y = ryf(x[i,0],x[i,1],n*h)
  k2x = rxf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y,n*h+.5*h)
  k2y = ryf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y,n*h+.5*h)
  k3x = rxf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y,n*h+.5*h)
  k3y = ryf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y,n*h+.5*h)
  k4x = rxf(x[i,0]+h*k3x,x[i,1]+h*k3y,n*h+h)
  k4y = ryf(x[i,0]+h*k3x,x[i,1]+h*k3y,n*h+h)
  x[i+1,0] = x[i,0] + h*(k1x+2*k2x+2*k3x+k4x)/6
  x[i+1,1] = x[i,1] + h*(k1y+2*k2y+2*k3y+k4y)/6
print x[n-1]
g = Gnuplot.Gnuplot(persist=1)
g.title('Nano1')
g.xlabel('x')
g.ylabel('y')
g('set data style lines')
g.plot (x) 