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

l2 = frec([], 'Bu ', 5)
print l2