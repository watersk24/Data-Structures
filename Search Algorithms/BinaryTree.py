#Author: Kevin Waters
#Date: 8 June 2020
#Description: This program implements a Binary Tree ADT. A binary tree consists of
#             a root node that contains a payload and left and right child nodes.
#             Each root node can have at most 2 children which are also binary trees.


class BinaryTree:
    def __init__(self, payload=None, leftChild=None, rightChild=None):
        """
        Class constructor

        :param payload: User entered value.
        :param leftChild: Node on Binary Tree. Default: None
        :param rightChild: Node on Binary Tree. Default: None
        """
        self.__payload = payload
        self.__leftChild = leftChild
        self.__rightChild = rightChild

    def getPayload(self):
        """
        Getter for class variable.
        :return: Returns value of payload.
        """
        return self.__payload

    def getLeftChild(self):
        """
        Getter for class variable.
        :return: Returns value of left child.
        """
        return self.__leftChild

    def getRightChild(self):
        """
        Getter for class variable.
        :return: Returns value of right child.
        """
        return self.__rightChild

    def setPayload(self, payload):
        """
        Setter for class variable.
        :param payload: Sets payload to user entered value.
        """
        self.__payload = payload

    def setLeftChild(self, leftChild):
        """
        Setter for class variable.
        :param leftChild: Sets leftChild to user entered value.
        """
        self.__leftChild = leftChild

    def setRightChild(self, rightChild):
        """
        Setter for class variable.
        :param rightChild: Sets RightChild to user entered value.
        """
        self.__rightChild = rightChild

    def isEmpty(self):
        return self.getPayload() is None

    def inorderTraversal(self):
        """
        Performs an inorder list traversal on a Binary Tree.
        :return: Returns value of leftChild of root node before returning root node.
        """
        result = ""
        if self.isEmpty():
            return result
        else:
            # Visit left node
            if self.getLeftChild() is not None:
                result += self.getLeftChild().inorderTraversal()

            # Visit root node
            result += " " + str(self.getPayload())

            # Visit right node
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().inorderTraversal()

            return result

    def preorderTraversal(self): # List traversal
        """
        Performs a preorder list traversal on a Binary Tree.
        :return: Returns root node before its children and descendants.
        """
        result = ""
        if self.isEmpty():
            return result
        else:
            # Visit root node
            result += str(self.getPayload())

            # Visit left node
            if self.getLeftChild() is not None:
                result += " " + self.getLeftChild().preorderTraversal()

            # Visit right node
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().preorderTraversal()

            return result

    def postorderTraversal(self):  # List traversal
        """
        Performs a postorder list traversal on a Binary Tree.
        :return: Returns root node after its children and descendants.
        """
        result = ""
        if self.isEmpty():
            return result
        else:
            # Visit left node
            if self.getLeftChild() is not None:
                result += self.getLeftChild().postorderTraversal()

            # Visit right node
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().postorderTraversal()

            # Visit root node
            result += " " + str(self.getPayload())

            return result

    def __str__(self):
        return self.inorderTraversal()


def myTest(): # test function to test functions of BinaryTree class
    BT = BinaryTree()
    print("BT is empty: ", BT.isEmpty())
    BT.setPayload(112)
    print("BT =", BT)
    print("BT is empty: ", BT.isEmpty())
    print(BT.getPayload())
    print("Left child = ", BT.getLeftChild())
    print("Right child = ", BT.getRightChild())
    BT.setLeftChild(BinaryTree(22))
    print("BT =", BT)
    print("Left child = ", BT.getLeftChild())
    BT.setRightChild(BinaryTree(24))
    print("BT =", BT)
    print("Right child = ", BT.getRightChild())


def main():
    BT = BinaryTree()
    print("isEmpty() = " + str(BT.isEmpty()))
    print(BT)

    BT.setPayload(101)
    print("isEmpty() = " + str(BT.isEmpty()))
    print(BT)

    BT.setLeftChild(BinaryTree(50))
    print(BT)

    BT.setRightChild(BinaryTree(250))
    print(BT)

    BT.getLeftChild().setLeftChild(BinaryTree(42))
    print(BT)

    BT.getLeftChild().getLeftChild().setLeftChild(BinaryTree(31))
    print(BT)

    BT.getRightChild().setRightChild(BinaryTree(315))
    print(BT)

    BT.getRightChild().setLeftChild(BinaryTree(200))
    print(BT)

    print("Inorder traversal: " + BT.inorderTraversal())
    print("Preorder traversal: " + BT.preorderTraversal())
    print("Postorder traversal: " + BT.postorderTraversal())


if __name__ == "__main__":
    main()
