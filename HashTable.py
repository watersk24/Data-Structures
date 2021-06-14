# Author: Kevin Waters
# Date: 16 June 2020
# Description: This program implements a Hash Table ADT.

from LinkedList.linkedList import linkedList
import random


class HashTableChaining:
    def __init__(self, size=61):
        """

        This algorithm uses linked lists for collision avoidance.

        :param size: (int) User entered value for size of Hash Table. If no value provided defaults to 61.
                    ***Note*** Size of Hash Table should be a prime number to avoid data loss.
        """
        self.__buckets = []
        for i in range(size):
            self.__buckets.append(linkedList())

    def __hash(self, value):
        """
        Hidden method that takes a user entered value from either the insert or find methods and returns the
        position where the value will be stored.

        :param value: User entered value.
        :return: Returns the position in the hash table where the user entered value will be stored.
        """
        return value % len(self.__buckets)

    def insert(self, value):
        """
        Inserts the user entered value into hash table.

        :param value: User entered value.
        :return: None
        """
        bucketNum = self.__hash(value)
        self.__buckets[bucketNum].append(value)

    def find(self, value):
        """

        Finds the user entered value in the hash table.
        :param value: Value to search for in hash table.
        :return: Returns the value.
        """
        bucketNum = self.__hash(value)
        result = self.__buckets[bucketNum].find(value)
        return result

    def __str__(self):
        """
        Overloads the string operator.
        :return: Returns the Hash Table as a string.
        """
        result = ""
        for i in range(len(self.__buckets)):
            result += "bucket " + str(i) + ": " + str(len(self.__buckets[i])) + ":"
            result += str(self.__buckets[i]) + "\n"
        return result


class HashTableProbing:
    def __init__(self, size=61):
        """

        This algorithm uses linear probing for collision avoidance.

        :param size: (int) User entered value for size of Hash Table. If no value provided defaults to 61.
                    ***Note*** Size of Hash Table should be a prime number to avoid data loss.
        """
        self.__buckets = [None] * size
        self.__skip = 3

    def __hash(self, value):
        """

        Hidden method that takes a user entered value from either the insert of find methods and returns the
        position where the value will be stored.

        :param value: User entered value.
        :return: Returns the position in the hash table where the user entered value will be stored.
        """
        # Returns the remainder of the value divided by the size of the hash table to compute the position in the table.
        return value % (len(self.__buckets))

    def __rehash(self, bucketNum):
        """
        Hidden method to rehash position values in the table. Used when inserting and finding values in the table.
        The addition of the skip ensures every position in the table will be visited.

        :param bucketNum: Position in hash table.
        :return: Returns the rehashed value.
        """
        return (bucketNum + self.__skip) % (len(self.__buckets))

    def insert(self, value):
        """
        Inserts value into hash table.

        :param value: User entered value.
        :return: None.
        """
        # Hashing value to get bucket number
        bucketNum = self.__hash(value)

        # Saving the original bucket number so we know when we've gone completely around the table.
        originalBucketNum = bucketNum

        # If bucket is not empty rehash with value so while loop will execute otherwise
        # originalBucketNum == bucketNum and loop will not execute.
        if (self.__buckets[bucketNum]) is not None:
            bucketNum = self.__rehash(bucketNum)

        # While loop looks for an empty bucket to insert value until it returns to originalBucketNum.
        while self.__buckets[bucketNum] is not None and bucketNum != originalBucketNum:
            bucketNum = self.__rehash(bucketNum)

        # If an empty bucket is found value is stored in bucket otherwise if no empty bucket is found
        # an exception is raised.
        if self.__buckets[bucketNum] is None:
            self.__buckets[bucketNum] = value
        else:
            raise Exception("Table full")

    def find(self, value):
        """
        Finds value in the hash table.
        :param value: Value to search for in hash table.
        :return: Returns value if found.
        """
        # Hashing value to get bucket number.
        bucketNum = self.__hash(value)

        # Saving the original bucket number so we know when we've gone completely around the table.
        originalBucketNum = bucketNum

        # If bucket is not empty rehash with value so while loop will execute otherwise
        # originalBucketNum == bucketNum and loop will not execute.
        if (self.__buckets[bucketNum]) is not None:
            bucketNum = self.__rehash(bucketNum)

        # While loop continues rehashing until value is found.
        while self.__buckets[bucketNum] is not None and self.__buckets[bucketNum] != value\
                and bucketNum != originalBucketNum:
            bucketNum = self.__rehash(bucketNum)

        # Returns value if found otherwise returns None.
        if self.__buckets[bucketNum] is not None and self.__buckets[bucketNum]:
            return self.__buckets[bucketNum]
        else:
            return None

    def __str__(self):
        """
        Overloads the string operator to return the hash table as a string.
        :return: Returns the Hash Table as a string.
        """
        result = ""
        for i in range(len(self.__buckets)):
            result += "bucket" + str(i) + ":" + str(self.__buckets[i]) + "\n"
        return result


def main():
    myHashTable = HashTableChaining()
    #myHashTable = HashTableProbing()

    for i in range(0, 30):
        j = random.randint(0, 50)
        myHashTable.insert(j)
    print(myHashTable)
    print("Hello")



if __name__ == "__main__":
    main()

