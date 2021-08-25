# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
import random as random
b = -1
a = .5
k = 1
f = .42
w = 1
c = 0.07
d1 = 0.2
delay = 6
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
  return -a*y1-b*x1-k*(x1**3)+f*cos(g)-d1*(y1**3)
def rx2f(x1,y1,x2,y2,t):
  return y2+c*(x1-x2)
def ry2f(x1,y1,x2,y2,t):
  g=w*t
  return -a*y2-b*x2-k*(x2**3)+f*cos(g)-d1*(y1**3)
h = 0.1
n = 20000
ni = int(delay/h)
print ni
x = zeros((n,5))
for i in range (0,ni+1):
  x[i,0] = random.uniform(0.5,1)
  x[i,1] = random.uniform(0,0)
  x[i,2] = random.uniform(.5,1)
  x[i,3] = random.uniform(0,0)
print x[0:ni+1]
for i in range (ni,n-1):
  k1x1 = rx1f(x[i,0],x[i,1],x[i-ni,2],x[i,3],i*h)
  k1y1 = ry1f(x[i,0],x[i,1],x[i,2],x[i,3],i*h)
  k1x2 = rx2f(x[i-ni,0],x[i,1],x[i,2],x[i,3],i*h)
  k1y2 = ry2f(x[i,0],x[i,1],x[i,2],x[i,3],i*h)
  k2x1 = rx1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i-ni,2],x[i,3]+.5*h*k1y2,i*h+.5*h)
  k2y1 = ry1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2,i*h+.5*h)
  k2x2 = rx2f(x[i-ni,0],x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2,i*h+.5*h)
  k2y2 = ry2f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2,i*h+.5*h)
  k3x1 = rx1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i-ni,2],x[i,3]+.5*h*k2y2,i*h+.5*h)
  k3y1 = ry1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2,i*h+.5*h)
  k3x2 = rx2f(x[i-ni,0],x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2,i*h+.5*h)
  k3y2 = ry2f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2,i*h+.5*h)
  k4x1 = rx1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i-ni,2],x[i,3]+h*k3y2,i*h+h)
  k4y1 = ry1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i,2]+h*k3x2,x[i,3]+h*k3y2,i*h+h)
  k4x2 = rx2f(x[i-ni,0],x[i,1]+h*k3y1,x[i,2]+h*k3x2,x[i,3]+h*k3y2,i*h+h)
  k4y2 = ry2f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i,2]+h*k3x2,x[i,3]+h*k3y2,i*h+h)
  x[i+1,0] = x[i,0] + h*(k1x1+2*k2x1+2*k3x1+k4x1)/6
  x[i+1,1] = x[i,1] + h*(k1y1+2*k2y1+2*k3y1+k4y1)/6
  x[i+1,2] = x[i,2] + h*(k1x2+2*k2x2+2*k3x2+k4x2)/6
  x[i+1,3] = x[i,3] + h*(k1y2+2*k2y2+2*k3y2+k4y2)/6
print x[n-1]
a = x[:,0:2]
b = x[:,2:4]
d =  zeros((n,2))
d[:,0] = x[:,0]-x[:,2]
d[:,1] = x[:,1]-x[:,3]
print a[n-1], b[n-1]
g = Gnuplot.Gnuplot()
g.title('Phase Space')
g.xlabel('x')
g.ylabel('y')
g('set data style lines')
h1 = Gnuplot.Gnuplot()
h2 = Gnuplot.Gnuplot()
h1.title('Time Series')
h1.xlabel('t')
h1.ylabel('x')
h1('set data style lines')
h2('set data style lines')
h2.xlabel('t')
h2.ylabel('y')
dp1 = Gnuplot.Gnuplot()
dp2 = Gnuplot.Gnuplot()
dp1('set data style lines')
dp1.title('x1-x2')
dp2('set data style lines')
dp2.title('y1-y2')
g.plot (a,b) 
h1.plot (x[:,0],x[:,2])
h2.plot (x[:,1],x[:,3])
dp1.plot(d[:,0])
dp2.plot(d[:,1])
plt = True
klo = float(raw_input('Do you want any more plots? 1/0 '))
if klo == 0: plt = False
while plt :
  m1 = float(raw_input('Range of Data Points(min) '))
  m2 = float(raw_input('Range of Data Points(max) '))
  am = a[m1:m2,:]
  bm = b[m1:m2,:]
  dm = d[m1:m2]
  g.title('Phase Space')
  g.xlabel('x')
  g.ylabel('y')
  g('set data style lines')
  h1.title('Time Series')
  h1.xlabel('t')
  h1.ylabel('x')
  h1('set data style lines')
  h2('set data style lines')
  h2.xlabel('t')
  h2.ylabel('y')
  dp1('set data style lines')
  dp1.title('x1-x2')
  dp2('set data style lines')
  dp2.title('y1-y2')
  g.plot (am,bm)
  h1.plot (x[(m1-1):(m2-1),0],x[(m1-1):(m2-1),2])
  h2.plot (x[(m1-1):(m2-1),1],x[(m1-1):(m2-1),3])
  dp1.plot(d[(m1-1):(m2-1),0])
  dp2.plot(d[(m1-1):(m2-1),1])
  g.hardcopy('Phase Space.ps', enhanced=1, color=1)
  h1.hardcopy('x.ps', enhanced=1, color=1)
  h2.hardcopy('y,ps', enhanced=1, color=1)
  dp1.hardcopy('diff1.ps',enhanced=1, color=1)
  dp2.hardcopy('diff2.ps',enhanced=1, color=1)
  klo = float(raw_input('Do you want any more plots? 1/0 '))
  if klo == 0:
    plt = False