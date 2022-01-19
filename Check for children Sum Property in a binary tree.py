class newNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sumTree(root):
    if root is None:
        return True
    else:
        if root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is not None:
            if root.val == root.left.val + root.right.val and sumTree(root.left) and sumTree(root.right):
                return True
            else:
                return False
        elif root.left is not None:
            if root.val == root.left.val and sumTree(root.left) and sumTree(root.right):
                return True
            else:
                return False
        elif root.right is not None:
            if root.val == root.right.val and sumTree(root.left) and sumTree(root.right):
                return True
            else:
                return False


root = newNode(10)
root.left = newNode(8)
root.right = newNode(2)
root.left.left = newNode(3)
root.left.right = newNode(5)
root.right.right = newNode(2)


if sumTree(root) == True:
    print("It is a sum tree.")
else:
    print("not")
    
    
    
'''

Ans=> It is a sum tree.

'''
