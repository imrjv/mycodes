class node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def isBalancedTree(root):
    if root is None:
        return True
    left = height(root.left)
    right = height(root.right)

    if abs(left-right) <= 1 and isBalancedTree(root.left) is True and isBalancedTree(root.right) is True:
        return True
    return False


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

if isBalancedTree(root):
    print("Tree is a Balanced binary tree!")
else:
    print("Tree is not a Balanced binary tree!")
