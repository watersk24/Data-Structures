""" Author: Kevin Waters
    Date: 3 June 2020
    Description: This file creates two classes for constructing a Linked List. Within the linked list class there are
                functions similar to the Python list functions for ease of use. Nodes may be added, removed, changed,
                and searched for."""


class listNode:
    def __init__(self, payload=None, next_node=None):
        """
        Constructor builds a node to be added to a linked list. Payload and next_node parameters are defaulted to None
        but either may be filled in by user.

        :param payload: Default to None.
        :param next_node: Default to None.

        """
        self.__payload = payload
        self.__nextListNode = next_node

    def getPayload(self):
        """
        Get method for payload.

        :return: Returns payload of list node.

        """
        return self.__payload

    def setPayload(self, payload):
        """
        Set method for payload.

        :param payload: User entered value.
        :return: None

        """
        self.__payload = payload

    def getNext(self):
        """
        Get method for next node in the linked list.

        :return: Returns next node in linked list.

        """
        return self.__nextListNode

    def setNext(self, next_node):
        """
        Set method for next list node in the linked list.

        :param next_node:
        :return: None

        """
        self.__nextListNode = next_node


class linkedList:

    def __init__(self):
        """
        Constructor builds empty list with default values: head = None, tail = None, size = 0.
        :return: None

        """
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        """
        Overloads the string function to return linked list as a string.

        :return: Linked list.

        """
        result = ""
        current = self.__head
        while current is not None:
            result = result + " " + str(current.getPayload())
            current = current.getNext()

        return result

    def __len__(self):
        """
        Overloads the length function to return the length of the linked list.

        :return: Length of the linked list.

        """
        return self.__size

    def __getIthNode(self, i):
        """

        :param i (int):  Index position of item in list.
        :return: Returns the item at index i.

        """
        if i < 0:
            i = self.__size + i

        elif i >= self.__size:
            raise IndexError("list index out of range")

        current = self.__head
        count = 0

        while current is not None and count < i:
            count += 1
            current = current.getNext()

        return current

    def insert(self, i, x):
        """
        Inserts a new node with user entered payload at the requested index position.

        :param i (int): Index position to insert new node.
        :param x: User entered value.

        """
        if self.isEmpty():
            self.__head = listNode(x)
            self.__tail = self.__head

        elif i <= 0:
            self.__head = listNode(x, self.__head)

        elif i >= self.__size:
            self.__tail.setNext(listNode(x))
            self.__tail = self.__tail.getNext()

        else:
            previous = self.__getIthNode(i - 1)
            previous.setNext(listNode(x, previous.getNext()))
            if self.__tail == previous:
                self.__tail = self.__tail.getNext()

        self.__size += 1

    def front(self):
        """
        Returns the payload of the first node in the linked list, if list is empty returns None.

        :return: Returns the node at the front of the linked list.

        """
        if self.isEmpty():
            return None
        else:
            return self.__head.getPayload()

    def back(self):
        """
        Returns the payload of the last node in the linked list, if list is empty returns None.

        :return: Returns the node at the back of the linked list.

        """
        if self.isEmpty():
            return None
        else:
            return self.__tail.getPayload()

    def isEmpty(self):
        """
        :return: Returns the boolean value True if linked list is empty otherwise returns False.

        """
        return self.__head is None

    def prepend(self, x):
        """
        Inserts node at beginning of linked list.

        :param x: User entered value.

        """
        self.insert(0, x)

    def append(self, x):
        """
        Inserts node at end of linked list.

        :param x: User entered value.

        """
        self.insert(len(self), x)

    def pop(self, i=None):
        """
        Removes node at index (i) of linked list. If no value for (i) is provided last node in list will be removed.
        If index value is out of range an error message is displayed.

        :param i: Index value of node.
        :return: Returns payload of node being removed from linked list.

        """

        if self.isEmpty():
            return None
        else:
            if i is None:   # Removes last item from list. pop()
                i = self.__size - 1
            if i == 0: # Removes first item in list. pop(0)
                x = self.__head.getPayload() #Save value before removing

                self.__head = self.__head.getNext() # Head moved to next node

                self.__size -= 1 # Decrement size of list by 1.

                if self.__head is None:
                    self.__tail = None

                return x

            else:
                previous = self.__getIthNode(i - 1)

                x = previous.getNext().getPayload()

                if self.__tail == previous.getNext():
                    self.__tail = previous

                previous.setNext(previous.getNext().getNext())

                self.__size -= 1

                return x

    def __getitem__(self, i):
        """
        Traverses linked list to return the payload of node at requested index value. If index value is out of
        range an error message is displayed.

        :param i(int): Index value.
        :return: Returns the payload at (i)th index.

        """
        try:
            return self.__getIthNode(i).getPayload()
        except IndexError:
            print("ERROR: Index value out of range.")

    def __setitem__(self, i, value):
        """
        Traverses linked list to requested index value and sets the payload to user entered value.
        If index value is out of range an error message is displayed.

        :param i (int): index value
        :param value: User entered value

        """
        try:
            self.__getIthNode(i).setPayload(value)
        except IndexError:
            print("ERROR: Index value out of range.")

    def find(self, x):
        """
        User enters a value x to traverse linked list and return payload if found.

        :param x: User entered value.
        :return: Returns payload if x equals the payload of current.

        """
        current = self.__head
        while current is not None:
            if current.getPayload() == x: # If current equals x return payload.
                return current.getPayload()
            else:
                current = current.getNext() # If current does not equal x get the next node.


def main():
    my_list = linkedList()
    print("my_list is Empty ==", my_list.isEmpty())
    print("The size of my_list is: ", len(my_list))
    print("The item at the front of my_list is: ", my_list.front())
    print("The item at the back of my_list is: ", my_list.back())
    print("my_list = " + str(my_list))
    print()
    my_list.insert(0, 3)
    print("my_list is Empty ==", my_list.isEmpty())
    print("The size of my_list is: ", len(my_list))
    print("The item at the front of my_list is: ", my_list.front())
    print("The item at the back of my_list is: ", my_list.back())
    print("my_list = " + str(my_list))
    print()
    my_list.insert(len(my_list), 5)
    print("my_list is Empty ==", my_list.isEmpty())
    print("The size of my_list is: ", len(my_list))
    print("The item at the front of my_list is: ", my_list.front())
    print("The item at the back of my_list is: ", my_list.back())
    print("my_list = " + str(my_list))
    print()
    my_list.insert(len(my_list) // 2, 21)
    print("The item at the front of my_list is: ", my_list.front())
    print("The item at the back of my_list is: ", my_list.back())
    print("my_list = " + str(my_list))
    print()
    my_list.prepend("qwe")
    print("The item at the front of my_list is: ", my_list.front())
    print("The item at the back of my_list is: ", my_list.back())
    print("my_list = " + str(my_list))
    print()
    my_list.append("zxc")
    print("The item at the front of my_list is: ", my_list.front())
    print("The item at the back of my_list is: ", my_list.back())
    print("my_list = " + str(my_list))
    print()
    print(my_list[0])
    print(my_list[3])
    print()
    my_list[5] = 7
    my_list[3] = 7
    print("my_list = " + str(my_list))
    print()
    print(my_list.find("hello"))
    print(my_list.find(21))
    my_list.pop()
    print("my_list = " + str(my_list))
    print()
    my_list.pop(0)
    print("my_list = " + str(my_list))
    my_list.pop(1)
    print("my_list = " + str(my_list))


if __name__ == "__main__":
    main()
