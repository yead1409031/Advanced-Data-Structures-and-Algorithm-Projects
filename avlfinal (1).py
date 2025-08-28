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
        def setBalance(self):
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
            ### WRITE YOUR CODE HERE ###
            elif self.left == None and self.right == None:
                yield self

            elif self.left != None:
                for leaf in self.left._getLeaves():
                    yield leaf

            elif self.right != None:
                for leaf in self.right._getLeaves():
                    yield leaf
                       
    def insert(self, item):

        def rotateRight(pivot):
            # pivot becomes right child of bad child
            # bad child's right child becomes pivot's left child

            # get pivot's left child node (bad child)
            leftChild = pivot.left

            ### WRITE YOUR CODE HERE ###
            rightGrandChild=leftChild.right
            leftChild.right=pivot
            pivot.left=rightGrandChild

            pivot.balance = 0
            leftChild.balance = 0
            
            # return bad child
            return leftChild
        
        def rotateLeft(pivot):
            # pivot becomes left child of bad child
            # bad child's left child becomes pivot's right child
            
            # get pivot's right child node (bad child)
            rightChild = pivot.right

            ### WRITE YOUR CODE HERE ###
            leftGrandChild=rightChild.left
            rightChild.left=pivot
            pivot.right=leftGrandChild

            pivot.balance = 0
            rightChild.balance = 0

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
                if self.pivotFound == False:
                    if root.balance != 0:
                        self.pivotFound = True
                    root.balance -= 1
                
                # check for Case 3 when AVL is unbalanced
                if root.getBalance() == -2:
                    # bad child must be left child, since we are in the left subtree
                    badChild = root.left

                    # Subcase A - Single Rotation
                    if item<badChild.item:
                        root= rotateRight(root)

                    # Subcase B - Double Rotation
                    if item>badChild.item:
                        root.left= rotateLeft(badChild)
                        root=rotateRight(root)

                        badGrandChild = badChild.right
                        if item == badGrandChild.item:
                            root.balance = 0
                            badChild.balance = 0
                        if item < badGrandChild.item:
                            root.balance = 1
                            badChild.balance = 0
                        if item > badGrandChild.item:
                            root.balance = 0
                            badChild.balance = -1
                                    
            # item to be inserted is larger than root, inserting into right subtree with specific rules to handle
            elif item > root.item:
                root.right = __insert(root.right, item)
                # handle Case 1 & Case 2 with no rotations
                if self.pivotFound == False:
                    if root.balance != 0:
                        self.pivotFound = True
                    root.balance += 1

                # check for Case 3 when AVL is unbalanced
                if root.getBalance() == 2:
                    # bad child must be right child, since we are in the right subtree
                    badChild = root.right
                    # Subcase A - Single Rotation
                    if item>badChild.item:
                        root= rotateLeft(root)
                    # Subcase B - Double Rotation
                    if item<badChild.item:
                        root.right= rotateRight(badChild)
                        root=rotateLeft(root)
                        badGrandChild = badChild.left
                        if item == badGrandChild.item:
                            root.balance = 0
                            badChild.balance = 0
                        if item < badGrandChild.item:                        
                            root.balance = 0
                            badChild.balance = 1
                        if item > badGrandChild.item:
                            root.balance = -1
                            badChild.balance = 0
            else:
                print(f"Insering duplicated value... {item}")
                raise Exception("Duplicate value")

            # once done __inserting return root
            return root
        
        # once done inserting update pivotFound value
        # and assign root with __insert return
        self.pivotFound = False
        self.root = __insert(self.root, item)

    # repr on tree calls repr on root node
    def __repr__(self):
        return f"AVLTree: {repr(self.root)}"

    # iter on tree calls iter on root node
    def __iter__(self):
        return iter(self.root)

    def __lookup(node, item):
        # returns True if value is in tree and False otherwise

        ### WRITE YOUR CODE HERE ###
        if node is None:
            return False   
        if item == node.item:
            return True
        elif item > node.item:
            return AVLTree.__lookup(node.right, item)

        # returns True or False
        return AVLTree.__lookup(node.left, item)

    def __contains__(self, item):
        # checks if item is in the tree
        # runs __lookup on the tree root
        return AVLTree.__lookup(self.root, item)

    def leaves(self):
        # finds tree leaves
        self.root._getLeaves()  

def main():
    tree = AVLTree()

    # get values from input file
    file = open('test-1.txt', "r")
    for line in file:
        values = line.split()

    print(f"Values to be inserted: {values}")
    print()
    
    # insert values into the AVL tree
    for v in values:
        tree.insert(int(v))
        print(f"Value {v} is inserted.")
    print()

    # print out the tree
    print(repr(tree))
    print()
    
    # print out tree in-order traversal
    print("In-order traversal: ", end = "")
    for node in tree:
        print(node, end = " ")    
    print()

    # print out tree leaves
    print("\nLeaves: ", end = "")
    tree.leaves()
    print()
    
    # check if given values are in the tree
    print()
    for val in [10, 17, 35, 38, 40]:
        if (val in tree):
            print(f"Value {val} is in tree")
        else:
            print(f"Value {val} is not in tree")  

main()