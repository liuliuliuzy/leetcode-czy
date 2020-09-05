class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sumNumbers(root)->int:
    if not root:
        return 0
    stack = [(root, str(root.val))]
    # res = []
    res = 0
    while stack:
        tmpNode, tmpStr = stack.pop()
        # res.append(tmpStr)
        if tmpNode.right:
            stack.append( (tmpNode.right, tmpStr+str(tmpNode.right.val)) )
        if tmpNode.left:
            stack.append( (tmpNode.left, tmpStr+str(tmpNode.left.val)) )
        if not tmpNode.left and not tmpNode.right:
            res+=int(tmpStr)
    # print(res)
    return res

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    print(sumNumbers(root))