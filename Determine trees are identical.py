class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if (root1.val == root2.val) and (identical(root1.left, root2.left) and identical(root1.right, root2.right)):
            return True
        else:
            return False
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
root2.left.left = Node(4)
root2.left.right = Node(5)

if identical(root1, root2):
    print("Trees are identical.")
else:
    print("Trees are not identical.")
    
    
    
    
"""
              1                         
            /   \
           2     3
         /   \
        4     5      Tree 1
        
        
        
              1
            /   \
           2     3
         /   \
        4     5           Tree 2
        
Ans => Trees are identical.

"""
