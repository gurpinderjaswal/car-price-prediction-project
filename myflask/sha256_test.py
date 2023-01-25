# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:14:29 2021

@author: Azmat
"""

from hashlib import sha256

x = 5
y = 0 #we don't know what y shd be yet.

while (sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0"):
    y += 1
print(f'The solution of y = {y}')