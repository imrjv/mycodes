class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def childrenSum(root):
    if root is None:
        return
    if root.left is not None and root.right is not None:
        if root.val > root.left.val + root.right.val:
            root.left.val = root.right.val = root.val
        elif root.val < root.left.val + root.right.val:
            root.val = root.left.val + root.right.val
    childrenSum(root.left)
    childrenSum(root.right)
    if root.left is not None and root.right is not None:
        if root.val != (root.left.val +root.right.val):
            root.val = root.left.val +root.right.val


root = Node(50)
root.left = Node(7)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(30)
root.right.left = Node(1)

childrenSum(root)

'''

To Check whether you have converted the given binary tree into Sum Tree. We can simply use the check for the sum tree algorithm. Put that check for the sum tree function
and implement it before and after the implementation of the convert function. That will show us the result.

'''
