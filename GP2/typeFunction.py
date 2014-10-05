# -+- coding: utf-8 -*-

import math
import random

print type(1), type(3.4), type((3+3j) + 2)
print type('treta'), type(True and False)
a = '1';
b = "Uma";

print type(a), type(b)
print type([1, 2, 3, [2,3]]), type((1,2,3))

class Teste:
   pass

print type(Teste)

obj = Teste()
print type(obj);

def func():
    return 3

print type(func)

print type(range(0,10))
print type(xrange(0,10))
print type(a > 10 if 10 else 2)
print type(a) ==  type("string") if "uma string" else "não sei"

print type((3+3j)+2.3)

def variance(l1):
   avg = sum(l1) / len(l1)

   y = reduce(lambda x,y: x+y, l1)
      
   var = y / (len(l1) - 1)

   return var

def randomList():
   x = 0
   l1 = []
   for i in range(0,100):
      l1.append(random.randint(0,200))
  # print l1

   return l1

print "Variance",
print variance(randomList())
