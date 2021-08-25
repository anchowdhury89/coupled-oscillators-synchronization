# -*- coding: utf-8 -*-
from numpy import *
import Gnuplot
b = -1
a = .5
k = 1
f = .37
w = 1
c1 = 0.3
c2 = -0.3
c3 = 0.3
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
def rx1f(x1,y1,x2):
  return y1+c1*(x2-x1)
def ry1f(x1,y1,t):
  g=w*t
  return -a*y1-b*x1-k*(x1**3)+f*cos(g)
def rx2f(x1,x2,y2,x3):
  return y2+c1*(x1-x2)+c2*(x3-x2)
def ry2f(x2,y2,t):
  g=w*t
  return -a*y2-b*x2-k*(x2**3)+f*cos(g)
def rx3f(x2,x3,y3,x4):
  return y3+c2*(x2-x3)+c3*(x4-x3)
def ry3f(x3,y3,t):
  g=w*t
  return -a*y3-b*x3-k*(x3**3)+f*cos(g)
def rx4f(x3,x4,y4):
  return y4+c3*(x3-x4)
def ry4f(x4,y4,t):
  g=w*t
  return -a*y4-b*x4-k*(x4**3)+f*cos(g)
h = 0.01
n = 200000
x = zeros((n,9))
x[0,0]=0
x[0,1]=0
x[0,2]=.5
x[0,3]=.5
x[0,4]=1
x[0,5]=1
x[0,6]=1.5
x[0,7]=1.5
for i in range (0,n-1):

  x[i,8] = i
  k1x1 = rx1f(x[i,0],x[i,1],x[i,2])
  k1y1 = ry1f(x[i,0],x[i,1],i*h)
  k1x2 = rx2f(x[i,0],x[i,2],x[i,3],x[i,4])
  k1y2 = ry2f(x[i,2],x[i,3],i*h)
  k1x3 = rx3f(x[i,2],x[i,4],x[i,5],x[i,6])
  k1y3 = ry3f(x[i,4],x[i,5],i*h)
  k1x4 = rx4f(x[i,4],x[i,6],x[i,7])
  k1y4 = ry4f(x[i,6],x[i,7],i*h)

  k2x1 = rx1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,x[i,2]+.5*h*k1x2)
  k2y1 = ry1f(x[i,0]+.5*h*k1x1,x[i,1]+.5*h*k1y1,i*h+.5*h)
  k2x2 = rx2f(x[i,0]+.5*h*k1x1,x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2,x[i,4]+.5*h*k1x3)
  k2y2 = ry2f(x[i,2]+.5*h*k1x2,x[i,3]+.5*h*k1y2,i*h+.5*h)
  k2x3 = rx3f(x[i,2]+.5*h*k1x2,x[i,4]+.5*h*k1x3,x[i,5]+.5*h*k1y3,x[i,6]+.5*h*k1x4)
  k2y3 = ry3f(x[i,4]+.5*h*k1x3,x[i,5]+.5*h*k1y3,i*h+.5*h)
  k2x4 = rx4f(x[i,4]+.5*h*k1x3,x[i,6]+.5*h*k1x4,x[i,7]+.5*h*k1y4)
  k2y4 = ry4f(x[i,6]+.5*h*k1x4,x[i,7]+.5*h*k1y4,i*h+.5*h)

  k3x1 = rx1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,x[i,2]+.5*h*k2x2)
  k3y1 = ry1f(x[i,0]+.5*h*k2x1,x[i,1]+.5*h*k2y1,i*h+.5*h)
  k3x2 = rx2f(x[i,0]+.5*h*k2x1,x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2,x[i,4]+.5*h*k2x3)
  k3y2 = ry2f(x[i,2]+.5*h*k2x2,x[i,3]+.5*h*k2y2,i*h+.5*h)
  k3x3 = rx3f(x[i,2]+.5*h*k2x2,x[i,4]+.5*h*k2x3,x[i,5]+.5*h*k2y3,x[i,6]+.5*h*k2x4)
  k3y3 = ry3f(x[i,4]+.5*h*k2x3,x[i,5]+.5*h*k2y3,i*h+.5*h)
  k3x4 = rx4f(x[i,4]+.5*h*k2x3,x[i,6]+.5*h*k2x4,x[i,7]+.5*h*k2y4)
  k3y4 = ry4f(x[i,6]+.5*h*k2x4,x[i,7]+.5*h*k2y4,i*h+.5*h)

  k4x1 = rx1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,x[i,2]+h*k3x2)
  k4y1 = ry1f(x[i,0]+h*k3x1,x[i,1]+h*k3y1,i*h+h)
  k4x2 = rx2f(x[i,0]+h*k3x1,x[i,2]+h*k3x2,x[i,3]+h*k3y2,x[i,4]+h*k3x3)
  k4y2 = ry2f(x[i,2]+h*k3x2,x[i,3]+h*k3y2,i*h+h)
  k4x3 = rx3f(x[i,2]+h*k3x2,x[i,4]+h*k3x3,x[i,5]+h*k3y3,x[i,6]+h*k3x4)
  k4y3 = ry3f(x[i,4]+h*k3x3,x[i,5]+h*k3y3,i*h+h)
  k4x4 = rx4f(x[i,4]+h*k3x3,x[i,6]+h*k3x4,x[i,7]+h*k3y4)
  k4y4 = ry4f(x[i,6]+h*k3x4,x[i,7]+h*k3y4,i*h+h)

  x[i+1,0] = x[i,0] + h*(k1x1+2*k2x1+2*k3x1+k4x1)/6
  x[i+1,1] = x[i,1] + h*(k1y1+2*k2y1+2*k3y1+k4y1)/6
  x[i+1,2] = x[i,2] + h*(k1x2+2*k2x2+2*k3x2+k4x2)/6
  x[i+1,3] = x[i,3] + h*(k1y2+2*k2y2+2*k3y2+k4y2)/6
  x[i+1,4] = x[i,4] + h*(k1x3+2*k2x3+2*k3x3+k4x3)/6
  x[i+1,5] = x[i,5] + h*(k1y3+2*k2y3+2*k3y3+k4y3)/6
  x[i+1,6] = x[i,6] + h*(k1x4+2*k2x4+2*k3x4+k4x4)/6
  x[i+1,7] = x[i,7] + h*(k1y4+2*k2y4+2*k3y4+k4y4)/6

p1 = x[:,0:2]
p2 = x[:,2:4]
p3 = x[:,4:6]
p4 = x[:,6:8]
q1 = zeros((n,2)); q2 = zeros((n,2)) ; q3 = zeros ((n,2)) ; q4 = zeros((n,2)); q5 = zeros((n,2)) ; q6 = zeros ((n,2))
q1[:,0] = x[:,0] ; q1[:,1] = x[:,2]
q2[:,0] = x[:,2] ; q2[:,1] = x[:,4]
q3[:,0] = x[:,4] ; q3[:,1] = x[:,6]
q4[:,0] = x[:,0] ; q4[:,1] = x[:,6]
q5[:,0] = x[:,0] ; q5[:,1] = x[:,4]
q6[:,0] = x[:,2] ; q6[:,1] = x[:,6]
s1 = Gnuplot.Gnuplot()
s2 = Gnuplot.Gnuplot()
s3 = Gnuplot.Gnuplot()
s4 = Gnuplot.Gnuplot()
v1 = Gnuplot.Gnuplot()
v2 = Gnuplot.Gnuplot()
v3 = Gnuplot.Gnuplot()
v4 = Gnuplot.Gnuplot()
v5 = Gnuplot.Gnuplot()
v6 = Gnuplot.Gnuplot()
s1.xlabel('x1') ; s2.xlabel('x2') ; s3.xlabel('x3') ; s4.xlabel('x4')
s1.ylabel('y1') ; s2.ylabel('y2') ; s3.ylabel('y3') ; s4.ylabel('y4')
v1.xlabel('x1') ; v2.xlabel('x2') ; v3.xlabel('x3') ; v4.xlabel('x1') ; v5.xlabel('x1') ; v6.xlabel('x2')
v1.ylabel('x2') ; v2.ylabel('x3') ; v3.ylabel('x4') ; v4.ylabel('x4') ; v5.ylabel('x3') ; v6.ylabel('x4')
s1('set data style lines') ; s2('set data style lines') ; s3('set data style lines') ; s4('set data style lines')
v1('set data style lines') ; v2('set data style lines') ; v3('set data style lines') ; v4('set data style lines') ; v5('set data style lines') ; v6('set data style lines') 
v1.plot(q1) ; v2.plot(q2) ; v3.plot(q3) ; v4.plot(q4) ; v5.plot(q5) ; v6.plot(q6)
plt = True
klo = float(raw_input('Do you want any more plots? 1/0 '))
if klo == 0: plt = False
while plt :
  m = float(raw_input('Enter no. of data points to be plotted '))
  q1m = q1[(n-m):n,:]
  q2m = q2[(n-m):n,:]
  q3m = q3[(n-m):n,:]
  q4m = q4[(n-m):n,:]
  q5m = q5[(n-m):n,:]
  q6m = q6[(n-m):n,:]
  v1.plot(q1m) ; v2.plot(q2m) ; v3.plot(q3m) ; v4.plot(q4m) ; v5.plot(q5m) ; v6.plot(q6m) 
  klo = float(raw_input('Do you want any more plots? 1/0 '))
  if klo == 0:
    plt = False