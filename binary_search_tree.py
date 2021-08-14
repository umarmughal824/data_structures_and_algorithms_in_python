class Node(object):
    """ Node of a tree """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    """ insert data in the tree """
    if root is None:
        self.root = Node(data)
    else:
        if root.data == data:
            return root
        if data < root.data:
            root.insert(root.left, data)
        else:
            root.insert(root.right, data)
    return root


def search(root, data):
    """ search the node in binary tree """
    if root is None:
        return None
    else:
        if root.data == data:
            return root
        else:
            if data < root.data:
                search(root.left, data)
            else:
                search(root.right, data)


def minimumValue(root):
    """ find the minimum value of the tree """
    if root is None:
        return None
    else:
        current = root
        while root.left is not None:
            current = current.left
        return current


def delete(root, data):
    """ delete the node """
    if root is None:
        return None
    else:
        if data < root.data:
            delete(root.left, data)
        elif data > root.data:
            delete(root.right, data)
        else:
            # If the node is with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # if both node exists, find the minimumValue node from the right subtree 
            # and swap it with the deleting node
            minimumNode = minimumValue(root.right)

            # replace the deleting node with the minimumValue node
            root.data = minimumNode.data

            # root.right = delete(root.right, minimumNode.data)
            delete(root.right, minimumNode.data)

        return root


def inOrder(root):
    """ In order traversal """
    if root:
        print(inOrder(root.left))
        print(root.data)
        print(inOrder(root.right))


def preOrder(root):
    """ pre order traversal """
    if root:
        print(root.data)
        print(preOrder(root.left))
        print(preOrder(root.right))


def postOrder(root):
    """ Post order traversal """
    if root:
        print(postOrder(root.left))
        print(postOrder(root.right))
        print(root.data)
