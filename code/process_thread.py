import os
import threading
import logging
import time
from alive_progress import alive_bar
from subprocess import run, CalledProcessError

pwd = os.path.dirname(__file__)

executable = os.path.join(pwd, os.pardir, "bin/example")
codeFile = os.path.join(pwd, os.pardir, "src/code.cpp")

inputFilePath = os.path.join(pwd, "inputs") # Multiple Cases
outputFilePath = os.path.join(pwd, "outputs") # Output for each testcase


def build():
    try:
        # print(f"Building Binary {example}.c")
        output = run(
            f'g++ {codeFile} -o {executable}',
            shell=True, capture_output=True, text=True)
    except CalledProcessError as err:
        print(f"Build Error : {err}")
    else:
        print(f"Return : {output.returncode}")
    return output.returncode


def executeCV(index, executable, inFile, outfile, errFile):
    try:
        # print(f"Running Binary {example}.c")
        output = run(
            f'{executable} < {inFile} > {outfile} 2> {errFile}',
            shell=True, capture_output=True, text=True)
    except CalledProcessError as err:
        print(f"Execute Error : {err}")
    else:
        pass
    return output.returncode


logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    build()
    executeThreads = []
    with alive_bar(len(os.listdir(inputFilePath))) as executeBar:
        for index, inputFile in enumerate(os.listdir(inputFilePath)):
            worker_thread = threading.Thread(target=executeCV, args=(
                index,
                executable,
                os.path.join(inputFilePath, inputFile),
                os.path.join(outputFilePath, f"output_{index}.txt"),
                os.path.join(outputFilePath, f"output_err_{index}.txt")
            ))
            executeThreads.append(worker_thread)
            time.sleep(0.3)
            worker_thread.start()
            executeBar()

    for index, worker in enumerate(executeThreads):
        worker.join()
