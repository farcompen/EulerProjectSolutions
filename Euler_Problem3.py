#! /usr/bin python
# -*- coding: utf-8 -*-
"""
he prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

from datetime import datetime

def asal(x):
    for a in xrange(3, x+1, 2):
        if x % a ==0 and a !=x :
            return "asal değil"
            break

        else :
            return "asal"
            break

baslangic_zamani = datetime.now()
print (baslangic_zamani)
deger = 600851475143
bolenler =[]
for a in xrange(3, deger+1, 2):

    if deger % a == 0:
        bolenler.append(a)
        deger = deger/a
        if deger == 1:
            break


bolenler_Tersten = bolenler[::-1]

for aranan in bolenler_Tersten:
    if asal(aranan) == "asal":
        print (aranan)
        print(datetime.now())
        break
