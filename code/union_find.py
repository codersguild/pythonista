# -*- coding: utf-8 -*-
import uuid


def returnIndex(data, elem):
    index = data.get(elem, None)
    if index is None:
        index = str(uuid.uuid4())
        data[elem] = index
    return index


def union(data, elem1, elem2):
    if (returnIndex(data, elem1) != returnIndex(data, elem2)):
        commonIndex = returnIndex(data, elem1)
        data[elem2] = commonIndex


def processExpressionImap(data, variables):
    if len(variables) == 1:
        returnIndex(data, variables[0])
    else:
        union(data, variables[0], variables[1])


if __name__ == "__main__":
    data = {}
    exprs = [["a"], ["a", "b"], ["b", "c"], ["d"], ["e"], ["e", "f"]]
    for elems in exprs:
        processExpressionImap(data, elems)
    print(data)
