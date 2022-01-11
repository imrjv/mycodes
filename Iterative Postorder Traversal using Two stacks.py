class Traversal:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder(root):
    if root is None:
        return
    stack = []
    new_stack = []
    stack.append(root)
    while len(stack) > 0:
        x = stack.pop()
        new_stack.append(x.val)
        if x.left is not None:
            stack.append(x.left)
        if x.right is not None:
            stack.append(x.right)
    while len(new_stack) != 0:
        print(new_stack.pop(), end=' ')


root = Traversal(1)
root.left = Traversal(2)
root.right = Traversal(3)
root.left.left = Traversal(4)
root.left.right = Traversal(5)
root.right.left = Traversal(6)
root.right.left.right = Traversal(7)
root.right.left.right.right = Traversal(8)

postorder(root)
