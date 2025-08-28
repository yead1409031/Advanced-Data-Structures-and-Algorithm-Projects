def __insert(root, item):
    # if empty tree, create a node with given item
    if root == None:
        return AVLTree.AVLNode(item)

    # item to be inserted is smaller than root
    # inserting into left subtree with specific rules to handle
    if item < root.item:
        root.left = __insert(root.left, item)

        # handle Case 1 & Case 2 with no rotations
        if root.getBalance() == 1:
            root.balance = 0
        elif root.getBalance() == 0:
            root.balance = -1
        else:
            # check for Case 3 when AVL is unbalanced
            badChild = root.left
            if badChild.getBalance() == -1:
                # Subcase A - Single Rotation
                root = rotateRight(root)
                root.balance = 0
                badChild.balance = 0
            else:
                # Subcase B - Double Rotation
                root.left = rotateLeft(badChild)
                root = rotateRight(root)
                if root.balance == 0:
                    badChild.balance = 0
                elif root.balance == -1:
                    badChild.balance = 1
                    root.balance = 0
                else:
                    badChild.balance = 0
                    root.balance = -1

    # item to be inserted is larger than root
    # inserting into right subtree with specific rules to handle
    elif item > root.item:
        root.right = __insert(root.right, item)

        # handle Case 1 & Case 2 with no rotations
        if root.getBalance() == -1:
            root.balance = 0
        elif root.getBalance() == 0:
            root.balance = 1
        else:
            # check for Case 3 when AVL is unbalanced
            badChild = root.right
            if badChild.getBalance() == 1:
                # Subcase A - Single Rotation
                root = rotateLeft(root)
                root.balance = 0
                badChild.balance = 0
            else:
                # Subcase B - Double Rotation
                root.right = rotateRight(badChild)
                root = rotateLeft(root)
                if root.balance == 0:
                    badChild.balance = 0
                elif root.balance == 1:
                    badChild.balance = -1
                    root.balance = 0
                else:
                    badChild.balance = 0
                    root.balance = 1

    # check if inserting duplicated value
    else:
        print(f"Insering duplicated value... {item}")
        raise Exception("Duplicate value")

    # once done __inserting return root
    return root
