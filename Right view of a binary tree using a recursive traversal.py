class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

stack = []
def rightView(root, level, stack):
    if root is None:
        return
    else:
        if level == len(stack):
            stack.append(root.val)
        rightView(root.right, level+1, stack)
        rightView(root.left, level+1, stack)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
rightView(root, 0, stack)
print(*stack)

'''
Ans => 1 3 7 8
Time Complexity = O(n)
'''
