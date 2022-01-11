class Traversal:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def all_traversal(root):
    stack = []
    pre = []
    post = []
    inorder = []
    stack.append([root, 1])
    while len(stack) > 0:
        p = stack[-1]
        if p[1] == 1:

            stack[-1][1] += 1
            pre.append(p[0].val)
            if p[0].left is not None:
                stack.append([p[0].left, 1])
        elif p[1] == 2:
            stack[-1][1] += 1
            inorder.append(p[0].val)
            if p[0].right is not None:
                stack.append([p[0].right, 1])
        else:
            post.append(p[0].val)
            stack.pop()
    else:
        print("PreOrder Traversal is", pre)
        print("InOrder Traversal is", inorder)
        print("PostOrder Traversal is", post)
