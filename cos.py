# -*- coding: utf-8 -*-
from numpy import *
x = float(raw_input("Enter value "))
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
#  print yprev, y
  n = n + 2
  err = abs(y-yprev)
print y