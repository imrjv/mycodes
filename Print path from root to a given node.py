class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def rootToNode(root, target, stack):
    if root is None:
        return False
    stack.append(root)
    node = stack[-1]
    if node.val == target:
        return True
    if node.left is not None and rootToNode(node.left, target, stack):
        return True
    elif node.right is not None and rootToNode(node.right, target, stack):
        return True
    else:
        stack.pop()
        return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


def path(root):
    stack = []
    target = 7
    rootToNode(root, target, stack)
    if len(stack) == 0:
        print("Element is not present in the tree.")
    else:
        for i in stack:
            print(i.val, end=' ')


path(root)

'''
                 1
               /   \
              2     3
             / \   /  \
            4   5  6   7
  
Ans => 1 3 7
Time Complexity => O(n) in the worst case.
'''
