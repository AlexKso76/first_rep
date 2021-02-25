#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:57:03 2021

@author: alexkso
"""
x=y=True
for i in range(0,2):
    for i in range(0,2):
        print('a: ', x, y, not x and not y)
        print('b: ', x, y,  x or (not x and y))
        print('c: ', x, y, (not x and y) or y)
        y=not y 
    x=not x
    