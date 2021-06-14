# Author: Kevin Waters
# Date: 18 June 2020
# Description: This program implements the Heap ADT. This data type uses a Python list to create a tree with
#              the property that the parent node is a smaller value than its children and all of its descendants.

import random


class Heap:
    def __init__(self):
        """
        Class constructor.
        """
        self.__size = 0 # Initializes size of list to 0.

        self.__heap = [None] # Creates an empty heap with None a index 0.

    def __len__(self):
        """
        Overloads the len operator.

        :return: Returns the number of values in the heap.
        """
        return self.__size

    def __getParent(self, i):
        """

        :param i: Position of node in heap.
        :return: Returns the position of parent at node i.
        """
        return i // 2

    def __getLeftChild(self, i):
        """

        :param i: Position of node in heap.
        :return: Returns the position of the left child of node i.
        """
        return i * 2

    def __getRightChild(self, i):
        """

        :param i: Position of node in heap.
        :return: Returns position of right child of node i.
        """
        return i * 2 + 1

    def isEmpty(self):
        """

        :return: Returns Boolean value True is heap is empty.
        """
        return self.__size == 0

    def __percolateUp(self, i):
        """
        __percolateUp method takes a value from insert function and places that value
        in appropriate position in heap to maintain a valid heap.

        :param i: Node in heap at index i in list
        :return: None
        """
        parent = self.__getParent(i)
        while parent > 0:
            # If parent has larger value than position i parent swaps with i
            if self.__heap[parent] > self.__heap[i]:
                self.__swap(parent, i)
                i = parent
                parent = self.__getParent(i)
            else:
                parent = 0 # stops loop

    def __percolateDn(self, i):
        """
        __percolateDn method takes a value from the deleteMin function and places that
        value in appropriate position in heap to maintain a valid heap.

        :param i: Node in heap at index i in list
        :return: None
        """
        lChild = self.__getLeftChild(i)
        rChild = self.__getRightChild(i)

        while (lChild <= self.__size):
            min = lChild
            if (rChild <= self.__size and self.__heap[rChild] < self.__heap[lChild]):
                min = rChild

            if (self.__heap[i] > self.__heap[min]):
                self.__swap(i, min)
                i = min
                lChild = self.__getLeftChild(i)
                rChild = self.__getRightChild(i)
            else:
                lChild = self.__size + 1

    def __swap(self, i, j):
        """
        Swaps parent node with node at position j in heap.

        :param i: Parent node
        :param j: Node in heap at index i in list
        :return: None
        """

        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def insert(self, x):
        """
        Inserts value into heap.

        :param x: User entered value.
        :return: None
        """
        # Increments size of heap by 1
        self.__size += 1
        # Appends value to end of heap.
        self.__heap.append(x)
        # Percolates value up the heap to appropriate position
        self.__percolateUp(self.__size)

    def deleteMin(self):
        """
        Removes and returns the minimum value of the heap.

        :return: Returns the minimum value in heap.
        """
        # Saves value at the root
        if self.__size < 1:
            return None
        value = self.__heap[1]
        # Moves the last value to position 1 and decrements the size of the heap.
        self.__heap[1] = self.__heap[self.__size]
        self.__size -= 1
        # Removes the last value from heap
        self.__heap.pop()
        # Percolate new value down
        self.__percolateDn(1)
        return value

    def getMin(self):
        """
        Returns minimum value in heap.

        :return: Returns the minimum value stored in the heap. Should always be at index 1 of list.
        """
        # Returns the minimum value in the heap
        return self.__heap[1]

    def __str__(self):
        """
        Overloads the string operator.

        :return: Returns the heap as a string.
        """
        result = ""

        return "myHeap = " + result + str(self.__heap[1:len(self.__heap)])


def main():
    myHeap = Heap()
    print("myHeap is empty: ", myHeap.isEmpty())
    for i in range(20):
        myHeap.insert(random.randint(0, 200))
    print(myHeap)
    print("myHeap is empty: ", myHeap.isEmpty())
    print("The size of myHeap is: ", len(myHeap))
    print("The minimum value in myHeap is: ", myHeap.getMin())

    for i in range(20):
        print("Deleted", myHeap.deleteMin(), "from myHeap.")
    print("The size of myHeap is: ", len(myHeap))
    print("myHeap is empty: ", myHeap.isEmpty())
    print(myHeap)

if __name__ == "__main__":
    main()