"""
Author: Kevin Waters
Date: 1 June 2020
Description: This file creates an abstract data type named Queue. Items are queued/dequeued to a list from
             index 0(front of queue), creating a First In First Out data structure. There is a built in
             method to view the next item in th queue as well as methods that return the length of the queue
             and if the queue is empty.

"""

import random


class Queue:
    def __init__(self):
        """
        Class constructor initializes an empty list

        """
        self.__items = []

    def enqueue(self, x):
        """
        Enqueue adds x to the front of the list(queue)

        """
        return self.__items.append(x)

    def dequeue(self):
        """
        Dequeue removes and returns the contents of the item at the front of the queue

        """
        return self.__items.pop(0)

    def peek(self):
        """
        Returns the value of the next item in the queue, if queue is empty returns None.

        """
        if self.isEmpty():
            return None

        else:
            return self.__items[len(self.__items) - 1]

    def len(self):
        """
        Returns the length of the queue.

        """
        return len(self.__items)

    def isEmpty(self):
        """
        Checks to see if the queue is empty and returns a boolean value True/False.

        """
        return len(self.__items) == 0



def main():
    myQueue = Queue()

    print("The queue is empty == ", myQueue.isEmpty())
    print("The size of the queue is: ", myQueue.len())
    print("The item at the back is: ", myQueue.peek(), "\n")

    for i in range(20):
        x = random.randint(-100, 100)
        print(x)
        myQueue.enqueue(x)

    print()
    print("The queue is empty == ", myQueue.isEmpty())
    print("The size of the queue is: ", myQueue.len())
    print("The item at the back is: ", myQueue.peek(), "\n")

    while not myQueue.isEmpty():
        x = myQueue.dequeue()
        print("Dequeued the value: ", x)

    print()
    print("The queue is empty == ", myQueue.isEmpty())
    print("The size of the queue is: ", myQueue.len())
    print("The item at the back is: ", myQueue.peek(), "\n")


if __name__ == "__main__":
    main()