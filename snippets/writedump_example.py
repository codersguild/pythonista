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
        
dump_rand_ints(fileptr, 100, 999999999, 15000000)

## Check and print Duplicates
## Astonishingly, there are no dup upto 1000000

fileptr = open("input.txt", "r")
mapping = dict()

for lines in fileptr.readlines() :
    if lines.rstrip() in mapping :
        mapping[lines.rstrip()] = "Duplicate"
    else :
        mapping[lines.rstrip()] = "First"
        
for elems in mapping :
    if mapping[elems] == "Duplicate" :
        print(elems)
