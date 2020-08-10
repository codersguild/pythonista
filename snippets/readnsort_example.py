'''
Input is a list of numbers.
N ==> No of elems in the lsit
N numbers ==> one number in each line. 

Eg : 
    
    20
115
 7
 4
     954
 784
 632
 152
 96
85
 23
     25
 41
 85
 96
45
 63
 17
94
38
     96
41
 

WAP to sort these numbers. 
'''

fileptr = open("input.txt", "r")

def bubbleSortVector(vec, N) :
    for i in range(N) :
        for j in range(i) : 
            if (vec[i] < vec[j]):
               vec[i], vec[j] = vec[j], vec[i]
    
N = int(fileptr.readline().strip())
vec = list()

for i in range(N):
    input_var = int(fileptr.readline().strip())
    vec.append(input_var)

bubbleSortVector(vec, N)

print(vec)
