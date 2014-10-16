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

lista =['a', 'b', 'c']
it = iter(lista)
print it
x1 = it.next()
print x1
x2 = it.next()
print x2

lista = ['a', 'b', 'c', 'd', 'e']
it = iter(lista)
x = it.next()
#while it:
#    print x
#    x = it.next()

print factorial_cauda(5)
print factorial(5)
l2 = frec([], 'Bu ', 2)
print l2

lista_linhas = ['           uma', '   duas', '         tres']

#expressão de geração -- devolve iterador
it = (linha.strip() for linha in lista_linhas)
print it.next() + it.next() + it.next()

total_letras = sum(len(linha.strip()) for linha in lista_linhas)
print " total de letras {0}".format(total_letras)

#compreensãp de lista -- devolve uma lista
lista = [linha.strip()
         for linha in lista_linhas
         if len(linha) > 7]
print lista
