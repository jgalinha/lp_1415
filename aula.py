#-*- coding: utf-8 -*-
__author__ = 'jbgal_000'

import math

def integral(f, a, b, N):
    """
    f(x) =  dx
    """
    dx = (b-a) / float(N)
    pontos = [f(a+dx*k) for k in range(N)]
    return sum(pontos)

def f(x):
    return x*x

def g(x): return math.log(x)

integral_1 = integral(f, 1.0, 4.0, 100)

print integral_1
