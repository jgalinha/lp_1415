# -*- coding: utf-8 -*-
# author 13077
# data: 05 de outubro de 2014
#


notas = {'P1': [6.0, 18.0],
         'SD': [6.0, 18.0],
         'AM': [6.0, 0.0],
         'FA': [6.0, 13.0],
         'AL': [6.0, 11.0],
         'P2': [7.0, 17.0],
         'MA': [7.0, 18.0],
         'MD': [6.0, 18.0],
         'PE': [6.0, 13.0],
         'ATT': [4.0, 18.0],
         'FSI': [6.0, 0.0],
         'MC': [6.0, 0.0],
         'RC1': [6.0, 18.0],
         'LP': [6.0, 0.0],
         'SO': [6.0, 0.0],
         'BD1': [6.0, 0.0],
         'Eng. Soft.': [6.0, 0.0],
         'EDA': [6.0, 0.0],
         'RC2': [6.0, 0.0],
         'IPC': [6.0, 0.0],
         'BD2': [7.0, 0.0],
         'HA': [6.0, 0.0],
         'SRC': [7.0, 0.0],
         'Empreendedorismo': [3.0, 18.0],
         'DGC': [3.0, 0.0],
         'PDE': [2.0, 0.0],
         'Portfolio': [2.0, 0.0],
         'PCR': [7.0, 0.0],
         'AS': [6.0, 18.0],
         'DI': [2.0, 0.0],
         'Estagio': [15.0, 0.0]}


def media(notasCurso):
    f0 = lambda x, y: x + y
    f1 = lambda x: notasCurso[x][0] if notasCurso[x][1] > 0 else 0
    f2 = lambda x: notasCurso[x][0] * notasCurso[x][1]

    return '{:.2f}'.format(reduce(f0, map(f2, notasCurso)) / reduce(f0, map(f1, notasCurso)))

print(u"Média : " + media(notas))

def media_alvo(notas, alvo, i=9.5):
    f0 = lambda x: notas[x][0] * notas[x][1] if notas[x][1] > 9.5 else notas[x][0] * i
    f1 = lambda x, y: x + y
    media_test = reduce(f1, map(f0, notas)) / reduce(f1, map(lambda x: notas[x][0], notas))
    if(media_test > alvo and media_test < (alvo + 0.5)):
        if media_test > 20:
            print 'Esquece lá isso!'
        else:
            print 'Necessita de uma média de {:.2f} nas restantes disciplinas para alcançar a média alvo de {:.2f}'.format(media_test, alvo)
        pass
    else:
        i += 0.1
        media_alvo(notas, alvo, i)

lista_medias = [12, 13, 14, 15, 16]
it_lista = iter(lista_medias)

media_alvo(notas, it_lista.next())




'''
lista = [1,2,3,4,5,4,4,2,3,5,2,6]

conj1 = set(lista)
conj2 = set([1,4,5,8])
conj3 = conj1.intersection(conj2)

lista1 = [x for x in conj1]

d = {}

d['a'] = 'x'
d['e'] = 'y'
d['i'] = 'z'
d['o'] = 't'
d['u'] = 'w'

frase = 'Cronus castrou o seu pai Urano'

f = lambda x: d[x] if x in d else x

frase3 = reduce(lambda x, y: x + y, map(f, frase))



def frec(l1, x, n):
    :param frec: devolve uma lista com n elementos x
    :param x: o elemento a repetir
    :param n: numero de repetições
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
'''