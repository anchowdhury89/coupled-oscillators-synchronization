# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
import random as random
import time as time
#parameter
b = -1; a = .5; k = 1; f = .37; w = 1; c = 0.138
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
  return -a*y1-b*x1-k*(x1**3)+f*cos(g)
def rx2f(x1,y1,x2,y2,t):
  return y2+c*(x1-x2)
def ry2f(x1,y1,x2,y2,t):
  g=w*t
  return -a*y2-b*x2-k*(x2**3)+f*cos(g)
# stepsize, iterations
h = 0.1; n = 10000; lst = 1500
x=zeros((n,4))
xf=zeros((n,4))
x[0,0] = 1.25; x[0,1] = 0; x[0,2] = -1.25; x[0,3] = 0
# RK4 module
for i in range (0,n-1):
  for j in range (0,4):
    xf[i,j] = round(x[i,j],2)
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
for j in range (0,4):
  xf[n-1,j] = round(x[n-1,j],3)
# plotting
# lag check
xr = (xf[n-lst:n,:]); xrd = (xf[n-2*lst:n,:])
a = xr[:,0:2]
b = xr[:,2:4]
d = zeros((lst,2))
d[:,0] = xr[:,0]-xr[:,2]; d[:,1] = xr[:,1]-xr[:,3]
print d[:,0]
d0min1 = (d[:,0]).argmin(); d0min2 = (d[d0min1+12:lst,0]).argmin(); # d0min2 is the lag
d1min1 = (d[:,1]).argmin(); d1min2 = (d[d1min1+12:lst,1]).argmin();
print d0min1; print d0min2
print d1min1; print d1min2
lag = (d0min2+12); print lag
lag1 = d1min2+12; print lag1
print xr[d0min1+10]; print xr[d0min1+lag1+10,:]
dp1 = Gnuplot.Gnuplot(persist=1); dp2 = Gnuplot.Gnuplot(persist=2); dp1('set data style lines'); dp2('set data style lines')
dp1.title('x1-x2'); dp2.title('y1-y2')
dp1.plot(xr[:,0],xr[:,2]); dp2.plot(d[:,0])
print time.clock()
