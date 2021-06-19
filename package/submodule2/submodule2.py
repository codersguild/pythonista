import time
import uuid
import os

from submodule1.auxiliary import JSONWrite

"""

How do we solve this?
Package whole module.

Traceback (most recent call last):
  File "package/submodule2/submodule2.py", line 3, in <module>
    from package.submodule1.auxiliary import printer
ModuleNotFoundError: No module named 'package'
"""


class DataElem(dict):
    def __init__(self, key="", data={}):
        self.key = key
        self.data = data
        self.uid = uuid.uuid4()
        # Make a serializable class
        dict.__init__(self, key=self.key, data=self.data,
                      unique_id=str(self.uid))

    def add_data(self, key="", data_item={}):
        self.data[key] = data_item


def main2(folder_name="", file_name=""):
    time.sleep(1)

    obj = DataElem(key="324", data={})
    obj.add_data("name", "Sumit")
    obj.add_data("affiliation", "IIT Kanpur")

    if not os.path.isdir(os.path.join(os.getcwd(), folder_name)):
        os.mkdir(os.path.join(os.getcwd(), folder_name))

    JSONWrite(os.path.join(os.getcwd(), folder_name, f"{file_name}.json"), obj)
