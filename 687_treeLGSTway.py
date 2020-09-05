class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def longestUnivaluePath(root)->int:
    ans = 0
    def arrow_length(node, tmp):
        if not node: return 0
        left_length = arrow_length(node.left, tmp)
        right_length = arrow_length(node.right, tmp)
        left_arrow = right_arrow = 0
        if node.left and node.left.val == node.val:
            left_arrow = left_length + 1
        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1
        tmp = max(tmp, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)

    arrow_length(root, ans)
    return ans

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    print(longestUnivaluePath(root))