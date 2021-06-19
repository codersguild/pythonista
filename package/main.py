from submodule1.submodule1 import main1
from submodule2.submodule2 import main2
from alive_progress import alive_bar

if __name__ == "__main__":
    calls = range(2)
    with alive_bar(2) as bar:
        bar.text("Called Main-1")
        bar()
        main1()
        bar.text("Called Main-2")
        bar()
        main2("data", "dump")
