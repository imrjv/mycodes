class Traversal:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while len(stack) > 0:
        x = stack.pop()
        print(x.val, end='')
        if x.right is not None:
            stack.append(x.right)
        if x.left is not None:
            stack.append(x.left)


root = Traversal(1)
root.left = Traversal(2)
root.right = Traversal(7)
root.left.left = Traversal(3)
root.left.right = Traversal(4)
root.left.right.left = Traversal(5)
root.left.right.right = Traversal(6)
preorder(root)
