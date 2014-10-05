# -*- coding: utf-8 -*-
# author 13077
# data: 05 de outubro de 2014
#

def frec(l1, x, n):
    '''
    :param frec: devolve uma lista com n elementos x
    :param x: o elemento a repetir
    :param n: numero de repetições
    '''
    if not n:
        return l1
    else:
        return [x] + frec(l1, x, n-1)

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_cauda(n):
    def fact(i=n, acc=1):
        if i == 0:
            return acc
        else:
            return fact(i-1, (acc * i))
    return fact()

print factorial_cauda(5)
print factorial(5)

l2 = frec([], 'Bu ', 2)
print l2
