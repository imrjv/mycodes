class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.val != root2.val:
            return False
        left = identical(root1.left, root2.left)
        right = identical(root1.right, root2.right)
        if left and right:
            return True
    else:
        return False


root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(5)
root2.left.right = Node(5)

if identical(root1, root2):
    print("Trees are identical.")
else:
    print("Tress are not identical.")
    
    
#  Ans => Tress are not identical.
