# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
a = 10
b = 28
c =  float(8.0/3.0)
def rxf(x,y):
  return a*(y-x)
def ryf(x,y,z):
  return b*x-y-x*z
def rzf(x,y,z):
  return x*y - c*z
h = 0.001
n = 300000
x = zeros((n,3))
x[0,0]=4
x[0,1]=2
x[0,2]=-4
for i in range (0,n-1):
  k1x = rxf(x[i,0],x[i,1])
  k1y = ryf(x[i,0],x[i,1],x[i,2])
  k1z = rzf(x[i,0],x[i,1],x[i,2])
  k2x = rxf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y)
  k2y = ryf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y,x[i,2]+.5*h*k1z)
  k2z = rzf(x[i,0]+.5*h*k1x,x[i,1]+.5*h*k1y,x[i,2]+.5*h*k1z)
  k3x = rxf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y)
  k3y = ryf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y,x[i,2]+.5*h*k2z)
  k3z = rzf(x[i,0]+.5*h*k2x,x[i,1]+.5*h*k2y,x[i,2]+.5*h*k2z)
  k4x = rxf(x[i,0]+h*k3x,x[i,1]+h*k3y)
  k4y = ryf(x[i,0]+h*k3x,x[i,1]+h*k3y,x[i,2]+h*k3z)
  k4z = rzf(x[i,0]+h*k3x,x[i,1]+h*k3y,x[i,2]+h*k3z)
  x[i+1,0] = x[i,0] + h*(k1x+2*k2x+2*k3x+k4x)/6
  x[i+1,1] = x[i,1] + h*(k1y+2*k2y+2*k3y+k4y)/6
  x[i+1,2] = x[i,2] + h*(k1z+2*k2z+2*k3z+k4z)/6
xm = x[(n-50000):n,:]
g = Gnuplot.Gnuplot(persist=1)
g.title('Lorenz System')
g.xlabel('x')
g.ylabel('y')
g.zlabel('z')
g('set data style lines')
g.splot (xm) 
print xm[n-1]