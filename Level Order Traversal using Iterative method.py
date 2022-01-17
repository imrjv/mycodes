class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrderTraversal(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].val, end=' ')
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

levelOrderTraversal(root)

'''
            10                      Answer => 10 2 10 20 1 -25 34
           /  \                     Time Complexity: O(n)
          2    10                   Space Complexity: O(n) 
         / \     \
       20   1    -25
                 /  \
                3    4
                
                
'''
