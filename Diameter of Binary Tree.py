class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diameter(root, maxi):
    if root is None:
        return 0

    lh = diameter(root.left, maxi)
    rh = diameter(root.right, maxi)

    maxi[0] = max(maxi[0], lh+rh+1)

    return 1+max(lh, rh)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.right.right.right = Node(10)

maxi = [0]
diameter(root, maxi)
print(maxi[0])

'''

Ans => 7
Time Complexity = O(n)

'''
