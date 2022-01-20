class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leftHeight(root):
    height = 0
    while root:
        height += 1
        root = root.left
    return height


def rightHeight(root):
    height = 0
    while root:
        height += 1
        root = root.right
    return height


def totalNodes(root):
    if root is None:
        return 0
    
    # Height of left subtree of the given root
    lh = leftHeight(root)
    # Height of right subtree of the given root
    rh = rightHeight(root)

    if lh == rh:
        return 2**lh - 1
    return 1 + totalNodes(root.left) + totalNodes(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(5)

print(totalNodes(root))


'''

Ans => 7
Time Complexity = O((logN)^2))
Space Complexity = O(1)

'''
