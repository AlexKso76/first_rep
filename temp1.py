#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 12:16:26 2021

@author: alexkso
"""

def search4vowels(phrase:str, latters:str='eeuioa')->set:
    """
    Returns
    -------
    None.

    """
    return set(latters).intersection(set(phrase))
print(search4vowels('zxcvbnim'))
