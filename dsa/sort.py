# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:00:04 2020
Checking module import
@author: lahir
"""
def sort_array (arr) :
    for i in range(len(arr)) :
        for j in range(i) :
            if (arr[i] < arr[j]) :
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)

