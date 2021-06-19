import json


def printer(filename, data):
    with open(filename, mode="w") as fileWritter:
        fileWritter.write(f"Data Elem : \n {data}\n")


def JSONWrite(filename, data):
    with open(filename, mode="w") as fileWritter:
        json.dump(data, fileWritter, indent=4, sort_keys=True)
