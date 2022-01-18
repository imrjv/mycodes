class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leftView(root, level, stack):
    if root is None:
        return
    if len(stack) == level:
        print(root.val, end=' ')
        stack.append(root.val)

    leftView(root.left, level+1, stack)
    leftView(root.right, level+1, stack)


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)
level = 0
stack = []
leftView(root, level, stack)


''' 
Ans => 10 2 7 14
