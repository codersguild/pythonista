# Open the file for input processing
input_file = open("input.txt", "r")

# Get the size and elements for the first array.
arr1__size = input_file.readline().rstrip()
arr1 = input_file.readline().rstrip().split(" ")

# Get the size and elements for the second array.
arr2__size = input_file.readline().rstrip()
arr2 = input_file.readline().rstrip().split(" ")

equal = []

for elem1 in arr1:
    for elem2 in arr2:
        if elem1 == elem2:
            print("Got Equal")
            equal.append(elem1)
