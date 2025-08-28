import sys

class AVLTree:
    def __init__(self, root = None):
        self.root = root

    class AVLNode:
        def __init__(self, item, balance = 0, left = None, right = None):
            self.item = item
            self.left = left
            self.right = right
            self.balance = balance

        def getBalance(self):
            return self.balance
        def setBalance(self, balance):
            self.balance = balance
        def __repr__(self):
            return f"AVLNode({repr(self.item)}, balance = {repr(self.balance)}, left = {repr(self.left)}, right = {repr(self.right)})"

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.item

            if self.right != None:
                for elem in self.right:
                    yield elem
                    
        def _getLeaves(self):
            # trivial case
            if self == None:
                return

            # leaf node
            if self.left == None and self.right == None:
                yield self

            if self.left != None:
                for leaf in self.left._getLeaves():
                    yield leaf

            if self.right != None:
                for leaf in self.right._getLeaves():
                    yield leaf
                       
    def insert(self, item):

        def rotateRight(pivot):
            # pivot becomes right child of bad child
            # bad child's right child becomes pivot's left child

            # get pivot's left child node (bad child)
            leftChild = pivot.left

            # pivot's left child becomes bad child's right child
            pivot.left = leftChild.right

            # bad child's right child becomes pivot
            leftChild.right = pivot

            # update pivot's balance factor
            if leftChild.balance == 1:
                pivot.balance = 0
                leftChild.balance = 0
            else:
                pivot.balance = 1
                leftChild.balance = -1

            # return bad child
            return leftChild
        
        def rotateLeft(pivot):
            # pivot becomes left child of bad child
            # bad child's left child becomes pivot's right child
            
            # get pivot's right child node (bad child)
            rightChild = pivot.right

            # pivot's right child becomes bad child's left child
            pivot.right = rightChild.left

            # bad child's left child becomes pivot
            rightChild.left = pivot

            # update pivot's balance factor
            if rightChild.balance == -1:
                pivot.balance = 0
                rightChild.balance = 0
            else:
                pivot.balance = -1
                rightChild.balance = 1

            # return bad child
            return rightChild

        def __insert(root, item):
            # if empty tree, create a node with given item
            if root == None:
                return AVLTree.AVLNode(item)

            # item to be inserted is smaller than root
            # inserting into left subtree with specific rules to handle
            if item < root.item:
                root.left = __insert(root.left, item)

                # handle Case 1 & Case 2 with no rotations
                if root.balance == 0:
                    root.balance = -1
                elif root.balance == 1:
                    root.balance = 0
                else:
                    self.pivotFound = True
                    badChild = root.left
                    if badChild.balance == -1:
                        root = rotateRight(root)
                    else:
                        root.left = rotateLeft(badChild)
                        root = rotateRight(root)

                # check for
