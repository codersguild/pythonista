from functools import reduce
import random
"""
For reading small files quickly.
Not recommended for large files.
"""
with open("./inputs/sample3.txt", mode="r") as file_ptr :
    str = file_ptr.read()

print(str)

"""
List Methods.
"""

fruits = ["apple", "mango", "orange", "banana"]
colors = ["red", "yellowish", "dark orange", "bright yellow"]
quantity = ["74", "21", "55", "88"]
numbers = []
fruit_map = dict()

"""
Enumerate a list.
"""
for (index, name) in enumerate(fruits) :
    print (f"{index + 1}. {name}")

"""
Zip lists
"""
for (fruit, color, qty) in zip(fruits, colors, quantity) :
    print (f"We have {qty} quantity of {fruit}, which is of {color} color")

"""
Functional Programming in Lists
"""
for j in range(10) :
    numbers.append(j)
    answer = reduce(lambda x, y : x * y, map(lambda a : a * a + 1, filter(lambda z : z % 2 == 0, numbers)))

print(answer)

"""
List Comprehension Technique.
"""
temp = [x for x in numbers if x % 3 == 0]
print(temp)

"""
Map Methods, Create, Read, Update and Delete operations.
"""
for fruit in fruits :
    id = random.randint(5, 600)
    fruit_map[id] = fruit
    one_key = id

print(fruit_map)

"""
Reads and Enumeration.
"""
for keys in fruit_map.keys() :
     print(keys)

for values in fruit_map.values() :
    print(values)

for (key, values) in fruit_map.items() :
    print(f"{key} ==> {values}")

query = fruit_map.get(random.randint(5, 600), "Fruit 404")
print(query)

query = fruit_map.get(one_key, "Fruit 404")
print(query)

"""
Update a map element.
"""
update = fruit_map.update({
        one_key : "pear"
    })

new_query = fruit_map.get(one_key, "Fruit 404")
print(new_query)

for (key, values) in fruit_map.items() :
    print(f"{key} ==> {values}")

"""
Delete map element. Returns the poped element.
"""
delete = fruit_map.pop(one_key)
print(delete)

for (key, values) in fruit_map.items() :
    print(f"{key} ==> {values}")
