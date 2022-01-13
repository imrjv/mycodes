class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maxpathsum(root):
    max_sum = 0
    if root is None:
        return 0
    else:
        left_height = maxpathsum(root.left)
        right_height = maxpathsum(root.right)

        max_sum = max(max_sum, left_height + right_height + root.val)
        max_val = max(left_height, right_height)+root.val
        if max_val < 0:
            return 0
        return max_val


root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(maxpathsum(root))

"""

              10
            /    \
          2       10
        /   \        \
      20     1       -25
                    /    \
                   3      4
                   
      *Maximum Path Sum of this binary is 42.
      
Output => 32
The code is incorrect. It needs some modifications, but it is almost there.

"""
    
