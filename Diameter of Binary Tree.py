class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diameter(root):
    max_height = 0
    if root is None:
        return 0
    else:

        left_height = diameter(root.left)
        right_height = diameter(root.right)

    max_height = max(max_height, left_height+right_height)
    return max(left_height, right_height) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.left.left.right = Node(9)
root.left.left.left.left = Node(10)

if diameter(root) > 0:
    print("The Diameter of a binary tree is", diameter(root)+1)
else:
    print(0)
    
    
# Ans => The Diameter of a binary tree is 6.
