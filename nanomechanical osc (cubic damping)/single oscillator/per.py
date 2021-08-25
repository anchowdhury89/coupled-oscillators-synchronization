# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
import random as random
b = -1
a = .5
k = 1
f = 0.38
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
  return -a*y1-b*x1-k*(x1**3)-d*y1**3+f*cos(g)
h = 0.01
n = 200000
x=zeros((n,2))
xf=ones((n,2))
x[0,0] = 1.5
x[0,1] = 0.8
for i in range (0,n-1):
  for j in range (0,2):
    xf[i,j] = round(x[i,j],3)
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
for j in range (0,2):
  xf[n-1,j] = round(x[n-1,j],3)
print x[n-1]
xr1 = xf[140000:]
xmin1 = xr1[:,0].argmin(); 
xr2 = xr1[xmin1+10:]
xmin2 = xr2[:,0].argmin();
xr3 = xr2[xmin2+10:]
xmin3 = xr3[:,0].argmin()
xr4 = xr3[xmin3+10:]
xmin4 = xr4[:,0].argmin()
xr5 = xr4[xmin4+10:]
xmin5 = xr5[:,0].argmin()
xr6 = xr5[xmin5+10:]
xmin6 = xr6[:,0].argmin()
print xmin1; print xmin2+10; print xmin3+10; print xmin4+10; print xmin5+10; print xmin6+10
g = Gnuplot.Gnuplot(persist=1)
g.title('Phase Space')
g.xlabel('x')
g.ylabel('y')
g('set data style lines')
h1 = Gnuplot.Gnuplot(persist=1)
h2 = Gnuplot.Gnuplot(persist=1)
g.plot(xr2[:,0])