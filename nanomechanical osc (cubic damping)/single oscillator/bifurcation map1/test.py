# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
import random as random
import time as time
b = -1
a = .5
k = 1
w = 1
da = 0.2
m = 2
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
  return -a*y1-b*x1-k*(x1**3)-da*y1**3+f*cos(g)
h = 0.01
n = 100000
fk = linspace(.39,.392,m)
np = int((n-20000)/630)+1
dat = zeros((m*np,2))
for j in range (0,m):
  f=fk[j]
  x=zeros((n,2))
  x[0,0] = 1
  x[0,1] = 0
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
  xr = x[60000:n]
  g=Gnuplot.Gnuplot(persist=1)
  g.plot(xr)
  for kd in range (0,n-61000,630):
    km=kd/630
    rd=(-1)**km
    dat[j*np+km,0] = fk[j];
    dat[j*np+km,1] = max(xr[kd:kd+630,0])
  print (j,time.clock())
savetxt('data.dat', dat)
print time.clock()