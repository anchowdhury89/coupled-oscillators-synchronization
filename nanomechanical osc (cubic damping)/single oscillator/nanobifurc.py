# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
import random as random
b = -1
a = .5
k = 1
w = 1
d = 0.2
mp = 5
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
def ry1f(x1,y1,t,f):
  g=w*t
  return -a*y1-b*x1-k*(x1**3)-d*y1**3+f*cos(g)
h = 0.1
n = 6000
fz = linspace(0,.5,mp)
np = int((n-2000)/62)+1
print np
l = zeros((mp*np,2))
for j in range (0,mp):
  x=zeros((n,2))
  x[0,0] = 0.4
  x[0,1] = 0.12
  fk = fz[j]
  print fk
  for i in range (0,n-1):
    k1x1 = rx1f(x[i,0],x[i,1],i*h)
    k1y1 = ry1f(x[i,0],x[i,1],i*h,fk)
    k2x1 = rx1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,i*h+.5*h)
    k2y1 = ry1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,i*h+.5*h,fk)
    k3x1 = rx1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,i*h+.5*h)
    k3y1 = ry1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,i*h+.5*h,fk)
    k4x1 = rx1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,i*h+h)
    k4y1 = ry1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,i*h+h,fk)
    x[i+1,0] = x[i,0] + h*(k1x1+2*k2x1+2*k3x1+k4x1)/6
    x[i+1,1] = x[i,1] + h*(k1y1+2*k2y1+2*k3y1+k4y1)/6
  print x
  xr = x[2000:n]
  for k in range (0,n-1000,62):
    km=k/62
    l[j*np+km,0] = fk;
    l[j*np+km,1] = xr[k,0]
print l