class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leaf(root):
    if root is None:
        return

    leaf(root.left)
    if root.left is None and root.right is None:
        print(root.val, end=' ')
    else:
        leaf(root.right)


def leftboundary(root):
    if root:
        if root.left:
            print(root.val, end=' ')
            leftboundary(root.left)
        elif root.right:
            print(root.val, end=' ')
            leftboundary(root.right)


def rightBoundary(root):
    if root is not None:
        if root.right:
            rightBoundary(root.right)
            print(root.val, end=' ')

        elif root.left:
            rightBoundary(root.left)
            print(root.val, end=' ')


def fullboundary(root):
    if root is None:
        return -1
    else:
        # Left Boundary Nodes including the root of the tree
        leftboundary(root)

        # Leaf Nodes of the tree
        leaf(root)

        # Right Boundary Nodes
        rightBoundary(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.right.right = Node(7)
root.right.left = Node(6)

fullboundary(root)


