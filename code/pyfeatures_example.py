nums = [1, 2, 3, 4, 5, 6, 7, 7, 8, 5, 3, 5, 7, 4]

"""
List Comprehension
"""
result1 = [x + 1 for x in nums]
result2 = [x % 2 for x in map(lambda y: y * y, nums)]

"""
Filter, Lambda & Map Examples
"""
result3 = [x for x in nums if x % 2 == 0]
result4 = [x for x in filter(lambda y: y % 2 == 0, nums)]

"""
Recursive Functions : No Memoization.
"""


def compute(x):
    return -x if x <= 1 else (compute(x - 1) + compute(x - 3) + compute(x - 5))


"""
Runs with Walrus Operator.
"""
result5 = [compute(x) for x in nums]
result6 = [y for x in nums if (y := compute(x)) % 2 == 0]

print(result1)
print(result2)
print(result4)

print(compute(7))
print(result5)
print(result6)

"""
List Comprehension
"""
y = [x * 3 for x in nums]

"""
Generator Expresion
"""
z = (x * 3 for x in nums)
print(z)
print(list(z))
