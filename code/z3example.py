# Inspired by the question asked by Presh Talwakar  : https://www.youtube.com/watch?v=vrI3vTQteDo
# I use Z3 tool by microsoft to solve it.

from z3 import *

x = Real('x')
y = Real('y')
a = Real('a')
b = Real('b')
s = Solver()
s.add(a >= 0)
s.add(b >= 0)
s.add(a + b == 100)
s.add(a * x == b * y)
s.add(a * y == 15)
s.add(b * x == 20 / 3)

if (s.check()):
    print(s.model())
