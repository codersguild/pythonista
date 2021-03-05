# -*- coding: utf-8 -*-


def isInt(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True


def isFloat(val):
    try:
        num = float(val)
    except ValueError:
        return False
    return True


def flatten(arr):
    if isinstance(arr, list) and len(arr) == 0:
        return arr
    if isinstance(arr[0], list):
        return flatten(arr[0]) + flatten(arr[1:])
    return arr[:1] + flatten(arr[1:])
