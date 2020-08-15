"""
TODOs
Task : Use Decorators to change use of sort_array()
Task : Sleep for random time secs not exceeding 25000
"""
from dsa.sort import *
import random
import time

num = [x for x in range(100)]
num.reverse()

sort_array(num)

time.sleep(random.randint(0, 25000))
