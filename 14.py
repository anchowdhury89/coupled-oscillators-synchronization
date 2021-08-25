# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
a = 10.0
b = 28.0
m = 1.0
c =  float(8.0/3.0)
def rxf(x,p):
  m = 1
  return p/m;
def ryf(x,p):
  return x-x**3
def en(x,p):
  return 0.5*p**2+-0.5*x**2+0.25*x**4
h = 0.001
n = 30000
x = zeros((n,3))
x[0,0]=0
x[0,1]=1
x[0,2]=en(x[0,0],x[0,1])
for i in range (0,n-1):
  k1x = rxf(x[i,0],x[i,1])
  k1y = ryf(x[i,0],x[i,1])
  k2x = rxf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y)
  k2y = ryf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y)
  k3x = rxf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y)
  k3y = ryf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y)
  k4x = rxf(x[i,0]+h*k3x,x[i,1]+h*k3y)
  k4y = ryf(x[i,0]+h*k3x,x[i,1]+h*k3y)
  x[i+1,0] = x[i,0] + h*(k1x+2*k2x+2*k3x+k4x)/6
  x[i+1,1] = x[i,1] + h*(k1y+2*k2y+2*k3y+k4y)/6
  x[i+1,2] = en(x[i,0],x[i,1])
xm = x[2000:n,:]
g = Gnuplot.Gnuplot(persist=1);e = Gnuplot.Gnuplot(persist=1)
g('set data style lines'); e('set data style dots'); 
g.plot (xm[:,0:2]) ;
e.plot (xm[:,2])