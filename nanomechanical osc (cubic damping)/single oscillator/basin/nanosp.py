# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
import random as random
import time as time
m = 100
z = zeros((m,2))
z[:,0] = linspace(-10,10,m)
z[:,1] = linspace(-10,10,m)
sc0 = zeros((m*m,3))
b = -1
a = .5
k = 1
f = 0.37
w = 1
d = 0.2
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
  return -a*y1-d*y1**3-b*x1-k*(x1**3)+f*cos(g)
h = .1
n = 3000
for zi in range(0,m):
  x = zeros((n,2))
  x[0,0] = z[zi,0]
  for zj in range(0,m):
    x[0,1] = z[zj,1]
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
    xr=x[(n-2*n/3):n,:]
#  g.title('Phase Space a = .5, b = -1, k = 1, w = 1, f = .37, d = 0.2')
#  g.xlabel('x')
#  g.ylabel('y')
#  g('set data style lines')
#  g.plot (a)
    xmin = abs(min(xr[:,0])); xmax = abs(max(xr[:,0]))
    sc0[zi*m+zj,0] = z[zi,0]
    sc0[zi*m+zj,1] = z[zj,1]
    if xmax < xmin:
      sc0[zi*m+zj,2] = 1
    else:
      sc0[zi*m+zj,2] = 2
print sc0
print time.clock()
savetxt('basindata.dat', sc0)
