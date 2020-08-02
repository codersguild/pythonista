# Dump random number to a file and 
# then to read it

# How can reads be optimized?
# Read in-memory. 

import random as rnd
import json as JSON

fileptr = open("input.txt", "w")

def dump_rand_ints (fileptr, start, end, length) :
    for i in range(length) :
        rnd_int = rnd.randint(start, end)
        fileptr.write(str(rnd_int) + "\n")
        
dump_rand_ints(fileptr, 100, 999999999, 8192)
