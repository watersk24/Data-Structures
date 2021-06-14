"""
Author: Kevin Waters
Date: 1 June 2020
Description: This file creates an abstract data type named Stack. Items are pushed to the stack(list) from
             index 0 and popped from the stack at index 0 creating a Last In First Out data structure. There is a built in
             method to view the next item in th queue as well as methods that return the length of the queue
             and if the queue is empty.

"""

import random


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, x):
        return self.__items.append(x)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        if self.isEmpty():
            return None

        else:
            return self.__items[len(self.__items) - 1]

    def len(self):
        return len(self.__items)

    def isEmpty(self):
        return len(self.__items) == 0


def main():
    myStack = Stack()

    print("The stack is empty == ", myStack.isEmpty())
    print("The size of the stack is: ", myStack.len())
    print("The item at the top is: ", myStack.peek(), "\n")

    for i in range(20):
        x = random.randint(-100, 100)
        print(x)
        myStack.push(x)

    print("Hello")
    print("The stack is empty == ", myStack.isEmpty())
    print("The size of the stack is: ", myStack.len())
    print("The item at the top is: ", myStack.peek(), "\n")

    while not myStack.isEmpty():
        x = myStack.pop()
        print("Popped the value", x, "from stack.")

    print()
    print("The stack is empty == ", myStack.isEmpty())
    print("The size of the stack is: ", myStack.len())
    print("The item at the top is: ", myStack.peek(), "\n")


if __name__ == "__main__":
    main()