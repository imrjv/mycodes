class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def naive(root):
    if root is None:
        return 0
    lh = naive(root.left)
    rh = naive(root.right)

    return 1+lh+rh


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(5)

print(naive(root))


'''

Ans => 7
Time Complexity = O(n)
Space Complexity = O(1)

There is an efficient way to this problem which is also present in this repository. Check for that approach.

''
