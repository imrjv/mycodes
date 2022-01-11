class Traversal:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return -1
    else:

        left_depth = height(root.left)
        right_depth = height(root.right)

        if left_depth > right_depth:
            return left_depth+1
        else:
            return right_depth+1


root = Traversal(1)
root.left = Traversal(2)
root.right = Traversal(3)
root.left.left = Traversal(4)
root.left.right = Traversal(5)
root.right.left = Traversal(6)
root.right.right = Traversal(7)

print(height(root))

# Ans => 2
