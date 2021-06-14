# Author: Kevin Waters
# Date: 17 June 2020
# Description: This program implements a Selection Sort algorithm.

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


def selectionSort(theList):
    """
        Sorts the Python list using the selection sort algorithm.

        :param theList: Python list
        :return: None
        """

    N = len(theList)
    i = N - 1
    stopEarly = False

    for i in range(N - 1):
        smallestPosition = i
        for j in range(i + 1, N):
            if theList[smallestPosition] > theList[j]:
                smallestPosition = j
        swap(theList, i, smallestPosition)


def main():
    myList = [random.randint(0, 1000) for i in range(300)]
    print("The sorted list = " + str(sorted(myList)))
    print("The unsorted list = " + str(myList))
    print("")
    startTime = time.time()
    selectionSort(myList)
    stopTime = time.time()
    print("After selection sort = " + str(myList))
    print("Time to selection sort = " + format(stopTime - startTime, "6.4f") + "seconds")



if __name__ == "__main__":
    main()
