# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:02:08 2019

@author: saura
"""

import re

emails = open('C:/Users/saura/Desktop/emails.txt').readlines()

x = re.search("\s",emails)

if (x):
    re.sub("^",'"',emails)
    re.sub("$",'",',emails)
    print(14)