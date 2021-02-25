#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:42:51 2021

@author: alexkso
"""

#volwes={ 'a', 'e', 'e', 'i', 'o', 'u', 'u' }
#print(volwes)

import temp1

vowels=set('aeiou')
word='hello'
vowels2=set(word)
u=vowels.union(vowels2)
d=vowels.difference(vowels2)
d2=vowels2.difference(vowels)
i=vowels.intersection(vowels2)
print(vowels)
print(vowels2)
print('diff', sorted(list(d)))
print('diff2', sorted(list(d2)))
print('union', sorted(list(u)))
print('intersection', sorted(list(i)))

q=temp1.summ(b=3, a=4)
print(q)