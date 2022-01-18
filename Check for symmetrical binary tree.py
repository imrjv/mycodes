class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def symmetrical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None and root1.val == root2.val:
        return symmetrical(root1.left, root2.right) and symmetrical(root1.right, root2.left)
    else:
        return False


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)


if symmetrical(root, root) == True:
    print("Symmetrical")
else:
    print("Not symmetrical")
    
'''

                1
              /   \
             2     2
            / \   / \
           4   3 3   4
           
Ans => Symmetrical
Time Complexity => O(n)
Space Complexity => O(h) where h is the maximum height of the binary tree

'''
