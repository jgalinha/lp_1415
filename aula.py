#-*- coding: utf-8 -*-
__author__ = 'jbgal_000'

import math

def integral(f, a, b, N):
    """
    f(x) =  dx
    """
    dx = (b-a) / float(N)
    #pontos = [f(a+dx*k) for k in range(N)
    pontos = map(lambda x: f(x)*dx, [a+k*dx for k in range(N)])
    return sum(pontos)

def f(x):
    return x*x

def g(x):
    return math.log(x)

integral_1 = integral(g, 1.0, 4.0, 1000000)

print integral_1

def l(x):
    return lambda x: x+1

print l(2)