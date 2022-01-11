class Traversal:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(x):
    if root is None:
        return
    stack = []
    stack.append(root)
    while len(stack) > 0:
        x = stack[-1]
        if x.left is not None:
            stack.append(x.left)
            continue

        x = stack.pop()
        print(x.val, end='')

        if len(stack) == 0:
            return

        x = stack.pop()
        print(x.val, end='')
        if x.right is not None:
            stack.append(x.right)


root = Traversal(1)
root.left = Traversal(2)
root.right = Traversal(3)
root.left.left = Traversal(4)
root.left.right = Traversal(5)

# Ans => 4 2 5 1 3
