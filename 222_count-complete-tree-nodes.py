# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def countNodesII(self, root: TreeNode) -> int:
        '''
        要利用到完全二叉树的性质
        '''
        def countHight(root: TreeNode) -> int:
            if not root:
                return 0
            return 1+countHight(root.left)
        
        if not root:
            return 0
        lh, rh = countHight(root.left), countHight(root.right)
        if lh == rh:
            return 1 + (1 << lh) - 1 + self.countNodesII(root.right)
        else:
            return 1 + (1 << (lh-1)) - 1 +self.countNodesII(root.left)

if __name__ == "__main__":
    s = Solution()
    x = TreeNode(1)
    x.left = TreeNode(2)
    x.right = TreeNode(3)
    x.left.left = TreeNode(4)
    x.left.right = TreeNode(5)
    x.right.left = TreeNode(6)
    print(s.countNodesII(x))
