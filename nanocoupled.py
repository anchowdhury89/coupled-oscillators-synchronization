# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
k1 = -1
b1 = .5
k3 = 1
a = 10
w = 1
c = .23191
def rx1f(x1,y1,x2,y2):
  return y1
def ry1f(x1,y1,x2,y2):
  return -b1*y1-k1*x1-k3*(x1**3)+c*(x1-x2)
def rx2f(x1,y1,x2,y2):
  return y2
def ry2f(x1,y1,x2,y2):
  return -b1*y2-k1*x2-k3*(x2**3)+c*(x2-x1)
h = 0.001
n = 50000
x = zeros((n,4))
x[0,0]=-1
x[0,1]=.1
x[0,2]=1
x[0,3]=-.1
for i in range (0,n-1):
  k1x1 = rx1f(x[i,0],x[i,1],x[i,2],x[i,3])
  k1y1 = ry1f(x[i,0],x[i,1],x[i,2],x[i,3])
  k1x2 = rx2f(x[i,0],x[i,1],x[i,2],x[i,3])
  k1y2 = ry2f(x[i,0],x[i,1],x[i,2],x[i,3])
  k2x1 = rx1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2)
  k2y1 = ry1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2)
  k2x2 = rx2f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2)
  k2y2 = ry2f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2)
  k3x1 = rx1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2)
  k3y1 = ry1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2)
  k3x2 = rx2f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2)
  k3y2 = ry2f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2)
  k4x1 = rx1f(x[i,0]+.5*h*k3x1,x[i,1]+.5*h*k3y1,x[i,2]+.5*h*k3x2,x[i,3]+.5*h*k3y2)
  k4y1 = ry1f(x[i,0]+.5*h*k3x1,x[i,1]+.5*h*k3y1,x[i,2]+.5*h*k3x2,x[i,3]+.5*h*k3y2)
  k4x2 = rx2f(x[i,0]+.5*h*k3x1,x[i,1]+.5*h*k3y1,x[i,2]+.5*h*k3x2,x[i,3]+.5*h*k3y2)
  k4y2 = ry2f(x[i,0]+.5*h*k3x1,x[i,1]+.5*h*k3y1,x[i,2]+.5*h*k3x2,x[i,3]+.5*h*k3y2)
  x[i+1,0] = x[i,0] + h*(k1x1+2*k2x1+2*k3x1+k4x1)/6
  x[i+1,1] = x[i,1] + h*(k1y1+2*k2y1+2*k3y1+k4y1)/6
  x[i+1,2] = x[i,2] + h*(k1x2+2*k2x2+2*k3x2+k4x2)/6
  x[i+1,3] = x[i,3] + h*(k1y2+2*k2y2+2*k3y2+k4y2)/6
print x[n-1]
g = Gnuplot.Gnuplot(persist=1)
g.title('Nano1')
g.xlabel('x')
g.ylabel('y')
g('set data style lines')
h = Gnuplot.Gnuplot(persist=1)
h.title('Nano2')
h.xlabel('x')
h.ylabel('y')
h('set data style lines')
a = x[:,0:2]
b = x[:,2:4]
print a[n-1], b[n-1]
g.plot (a,b)
#h.plot (b)
plt = True
klo = float(raw_input('Do you want any more plots? 1/0 '))
if klo == 0: plt = False
while plt :
  m = float(raw_input('Enter no. of data points to be plotted '))
  am = a[(n-m):n,:]
  bm = b[(n-m):n,:]  
  g.plot (am,bm)
  klo = float(raw_input('Do you want any more plots? 1/0 '))
  if klo == 0:
    plt = False
