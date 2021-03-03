import sys
import functools

n = input().strip().split(' ')
print(functools.reduce(lambda a, b: a * b,
                       [sum(list(map(int, x))) for x in n]))
