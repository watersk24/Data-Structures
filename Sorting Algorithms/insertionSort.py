# Author: Kevin Waters
# Date: 17 June 2020
# Description: This program implements an Insertion Sort algorithm.

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


def insertionSort(theList):
    """
        Sorts the Python list using the insertion sort algorithm.

        :param theList: Python list
        :return: None
        """

    N = len(theList)
    i = N - 1

    for i in range(1, N):
        holdValue = theList[i]
        j = i
        while j > 0 and theList[ j -1] > holdValue:
            theList[j] = theList[j - 1]
            j -= 1

            theList[j] = holdValue


def main():
    myList = [random.randint(0, 1000) for i in range(300)]
    print("The sorted list = " + str(sorted(myList)))
    print("The unsorted list = " + str(myList))
    print("")
    startTime = time.time()
    insertionSort(myList)
    stopTime = time.time()
    print("After insertion sort = " + str(myList))
    print("Time to insertion sort = " + format(stopTime - startTime, "6.4f") + " seconds")


if __name__ == "__main__":
    main()
