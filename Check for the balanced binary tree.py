class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_balancing(root):
    if root is None:
        return 0
    else:
        left_height = check_balancing(root.left)
        right_height = check_balancing(root.right)

        if (left_height == -1 or right_height == -1) or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height)+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)

if check_balancing(root) != -1:
    print("Tree is balanced")
else:
    print("Tree is not balanced")
    
  # Ans => Tree is balanced
