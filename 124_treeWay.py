class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def __init__(self):
#         self.maxSum = float("-inf")

def maxPathSum(root: TreeNode) -> int:
    maxSum = float("-inf")
    def maxGain(node):
        if not node:
            return 0

        # 递归计算左右子节点的最大贡献值
        # 只有在最大贡献值大于 0 时，才会选取对应子节点
        leftGain = max(maxGain(node.left), 0)
        rightGain = max(maxGain(node.right), 0)
        
        # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
        priceNewpath = node.val + leftGain + rightGain
        
        # 更新答案
        maxSum = max(maxSum, priceNewpath)
    
        # 返回节点的最大贡献值
        return node.val + max(leftGain, rightGain)

    maxGain(root)
    return maxSum

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    
    print(maxPathSum(root))