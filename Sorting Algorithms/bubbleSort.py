# Author: Kevin Waters
# Date: 17 June 2020
# Description: This program implements a Bubble Sort algorithm.

import random
import time


def swap(theList, i, j):
    """
    Swaps the position of parameter i with parameter j.

    :param theList: Python list
    :param i: Position in list.
    :param j: Position in list.
    :return: None
    """
    temp = theList[i]
    theList[i] = theList[j]
    theList[j] = temp


def bubbleSort(theList):
    """
    Sorts the Python list using the bubble sort algorithm.

    :param theList: Python list
    :return: None
    """
    N = len(theList)
    i = N - 1
    stopEarly = False

    while i > 0 and not stopEarly:
        stopEarly = True

        for j in range(0, i):
            if theList[j] > theList[j + 1]:
                swap(theList, j, j + 1)
                stopEarly = False
        i -= 1


def main():
    myList = [random.randint(0, 1000) for i in range(3000)]
    print("The sorted list = " + str(sorted(myList)))
    print("The unsorted list = " + str(myList))
    print("")
    startTime = time.time()
    bubbleSort(myList)
    stopTime = time.time()
    print("After bubble sort = " + str(myList))
    print("Time to bu bubble sort = " + format(stopTime - startTime, "6.4f") + "seconds")


if __name__ == "__main__":
    main()
