class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, x, y):
    if root is None:
        return None
    if root.val == x or root.val == y:
        return root
    else:
        left = lowestCommonAncestor(root.left, x, y)
        right = lowestCommonAncestor(root.right, x, y)

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right.right = Node(7)

x = 10
y = 22
print(lowestCommonAncestor(root, x, y).val)

'''
                20
               /  \
              8    22
             / \     \
            4   12    25
               /  \
              10   14
              
              
Ans => 20
Time Complexity => O(n)

'''
