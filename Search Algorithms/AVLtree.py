# Author: Kevin Waters
# Date: 10 June 2020
# Description: This program implements the AVL Tree ADT. This data type maintains the properties of the
#              Binary Search Tree but adds functionality to maintain a balanced tree such that there is not a
#              difference in height of 2 or more between the grandchildren of a root. This balancing of the tree
#              is an improvement of the Binary Search Tree by keeping the big-oh from degrading to O(N) for
#              the insert and find functions.

from BinaryTree import BinaryTree
from BinarySearchTree import BinarySearchTree


class AVLtree(BinarySearchTree, BinaryTree):

    def insert(self, x):
        """
                Inserts user entered value at the appropriate position in the BinarySearchTree.

                :param x: User entered value.
                :return: None
                """
        if self.isEmpty():  # base case for empty tree
            self.setPayload(x)
            return self

        elif x < self.getPayload():
            # If <= operator is used a duplicate of a payload will be
            # inserted before the original. < operator is used to maintain
            # the ordering.
            if self.getLeftChild() is None:
                # If there is no left subtree one is created with value x
                self.setLeftChild(AVLtree(x))
                self.computeHeight()
                return self
            else:  # Recursively insert into left subtree
                self.setLeftChild(self.getLeftChild().insert(x))
                if not self.balanced():
                    # Case 1:
                    if x < self.getLeftChild().getPayload():
                        return self.rotateWithLeftChild()

                    # Case 2
                    else:
                        self.setLeftChild(self.getLeftChild().rotateWithRightChild())
                        return self.rotateWithLeftChild()
                self.computeHeight()
                return self
        else:  # base case for x >= self.payload
            if self.getRightChild() is None:
                # If there is no right subtree one is created with value x
                self.setRightChild(AVLtree(x))
                self.computeHeight()
                return self
            else:  # Recursively insert into right subtree
                self.setRightChild(self.getRightChild().insert(x))
                if not self.balanced():
                    # Case 4:
                    if x >= self.getRightChild().getPayload():
                        return self.rotateWithRightChild()

                    # Case 3:
                    else:
                        self.setRightChild(self.getRightChild().rotateWithLeftChild())
                        return self.rotateWithRightChild()
                self.computeHeight()
                return self

    def balanced(self):
        """
        Performs a check to see if AVLtree is balanced.

        :return: Boolean value True if AVLtree is balanced otherwise returns False.
        """
        if self.getLeftChild() is not None:
            lHeight = self.getLeftChild().getHeight() # Sets variable lHeight to height of left child.
        else:
            lHeight = -1 # Returns -1 if left child is empty

        if self.getRightChild() is not None:
            rHeight = self.getRightChild().getHeight()  # Sets variable rHeight to height of right child.
        else:
            rHeight = -1 # Returns -1 if right child is empty
        return (abs(lHeight - rHeight) < 2) # Calculates if there is a difference of 2 or more between children
                                            # in AVLtree.

    def rotateWithLeftChild(self):
        """
        Left rotation occurs when an imbalance is detected in the left grandchild of self. Performs a left rotation
        of k1 where self becomes the right child of k1 maintaining the properties of the Binary Search Tree.
        Since k1s right child is greater then k1, the right child now becomes the left child of self.
        :return: Returns new root node k1.
        """
        k1 = self.getLeftChild()

        # move right child of k1 to left child of self
        self.setLeftChild(k1.getRightChild())

        # Self becomes right child of k1
        k1.setRightChild(self)

        # Recompute heights
        self.computeHeight()
        k1.computeHeight()

        return k1

    def rotateWithRightChild(self):
        """
        Right rotation occurs when an imbalance is detected in the right grandchild of self. Performs a right rotation
        of k2 where self becomes the left child of k2 maintaining the properties of the Binary Search Tree.
        Since k2s left child is greater then self, the left child now becomes the right child of self.
        :return: Returns new root node k2.
        """
        k2 = self.getRightChild()

        # move right child of k1 to left child of self
        self.setRightChild(k2.getLeftChild())

        # Self becomes right child of k1
        k2.setLeftChild(self)

        # Recompute heights
        self.computeHeight()
        k2.computeHeight()

        # Returning new root
        return k2


def main():
    avlBST = AVLtree()
    print(avlBST.isEmpty())
    avlBST = avlBST.insert(63)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(2)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(-10)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(-15)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(81)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(89)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(93)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(4)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(6)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(20)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(17)
    print("avlBST = ", avlBST)
    avlBST = avlBST.insert(23)
    print("avlBST = ", avlBST)


if __name__=="__main__":
    main()