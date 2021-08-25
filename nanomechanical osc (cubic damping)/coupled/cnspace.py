# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
import time as time
#parameter
b = -1; a = .5; k = 1; f = .42; w = 1; da = 0.2; c = 0.1
m = 100
z = zeros((m,3))
z[:,0] = linspace(-1.5,1.5,m)
z[:,1] = linspace(-1.5,1.5,m)
sc0 = zeros((m*m,3))
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
def rx1f(x1,y1,x2,y2,t):
  return y1+c*(x2-x1)
def ry1f(x1,y1,x2,y2,t):
  g=w*t
  return -a*y1-da*y1**3-b*x1-k*(x1**3)+f*cos(g)
def rx2f(x1,y1,x2,y2,t):
  return y2+c*(x1-x2)
def ry2f(x1,y1,x2,y2,t):
  g=w*t
  return -a*y2-da*y2**3-b*x2-k*(x2**3)+f*cos(g)
# stepsize, iterations
h = .1; n = 6000
x=zeros((n,4))
x[0,0] = 0; x[0,3] = 0;
# Run a loop over different x1(0) and x2(0)
for zi in range(0,m):
  x[0,1] = z[zi,0]
  for zj in range(0,m):
    x[0,3] = z[zj,1]
    # RK4 module
    for i in range (0,n-1):
      k1x1 = rx1f(x[i,0],x[i,1],x[i,2],x[i,3],i*h)
      k1y1 = ry1f(x[i,0],x[i,1],x[i,2],x[i,3],i*h)
      k1x2 = rx2f(x[i,0],x[i,1],x[i,2],x[i,3],i*h)
      k1y2 = ry2f(x[i,0],x[i,1],x[i,2],x[i,3],i*h)
      k2x1 = rx1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2,i*h+.5*h)
      k2y1 = ry1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2,i*h+.5*h)
      k2x2 = rx2f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2,i*h+.5*h)
      k2y2 = ry2f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2,i*h+.5*h)
      k3x1 = rx1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2,i*h+.5*h)
      k3y1 = ry1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2,i*h+.5*h)
      k3x2 = rx2f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2,i*h+.5*h)
      k3y2 = ry2f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2,i*h+.5*h)
      k4x1 = rx1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i,2]+h*k3x2,x[i,3]+h*k3y2,i*h+h)
      k4y1 = ry1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i,2]+h*k3x2,x[i,3]+h*k3y2,i*h+h)
      k4x2 = rx2f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i,2]+h*k3x2,x[i,3]+h*k3y2,i*h+h)
      k4y2 = ry2f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i,2]+h*k3x2,x[i,3]+h*k3y2,i*h+h)
      x[i+1,0] = x[i,0] + h*(k1x1+2*k2x1+2*k3x1+k4x1)/6
      x[i+1,1] = x[i,1] + h*(k1y1+2*k2y1+2*k3y1+k4y1)/6
      x[i+1,2] = x[i,2] + h*(k1x2+2*k2x2+2*k3x2+k4x2)/6
      x[i+1,3] = x[i,3] + h*(k1y2+2*k2y2+2*k3y2+k4y2)/6
    xr=x[(5*n/6):n,:]
    print (zi,zj)
    # Check if the oscillators are completely synchronized
    d =  zeros((n/6,2)); d[:,0] = xr[:,0]-xr[:,2]; d[:,1] = xr[:,1]-xr[:,3]
    dxmax = abs(max(d[:,0])); dymax =  abs(max(d[:,1])); dmax = max(dxmax, dymax);
    xmin = abs(min(xr[:,0])); xmax = abs(max(xr[:,0]))
    sc0[zi*m+zj,0] = z[zi,0]
    sc0[zi*m+zj,1] = z[zj,1]
    if dmax < 10**(-3):
    # Check potential well
      if xmax < xmin:
	sc0[zi*m+zj,2] = 1
      else:
	sc0[zi*m+zj,2] = 2
print time.clock()
savetxt('data.dat', sc0)