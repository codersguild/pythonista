import os
import sys

# COMMENT : Snippet-1
# Check if all elems of list pass a predicate
# Over the array, indicator function

results = [90, 89, 7655]

if all(x < 100 for x in results):
  print("All elements are more than 100 in this list")

# COMMENT : Snippet-2
# Check if directory exists

if not os.path.isdir("models"):
   os.mkdir("models")
    
# Terse processing from a line
lines = ["key0 : value0", "key1 : value1"]
lines[0].strip().split(":")[1].strip()
