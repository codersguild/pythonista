"""
Query Format :

    N_factor query_limit
    query_type query1 query2
    query_type query1 query2
    ...
    (...query_limit)

Eg : 
    
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1

How to read it?
"""

# Open the file for input processing
fptr = open("input.txt", "r");

# Read N-factor & the no.of Queries
# Split and store in an array.
first_line = fptr.readline().rstrip().split()

# Extract the data from the split. 
N_factor = int(first_line[0])
query_limit = int(first_line[1])

# List of queries in a map, 
# First is query type and second in query. 
query_mapping = []

# 0 to query_limit
for _ in range(query_limit):
    query_mapping.append(list(map(int, fptr.readline().rstrip().split())))
    
for elem in query_mapping:
    print("Type : " + str(elem[0]))
    print("query1 : " + str(elem[1]))
    print("query2 : " + str(elem[2]))
    print("\n")
    
