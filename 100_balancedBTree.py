# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(node: TreeNode) -> int:
            if node == None:
                return 0 
            return max(getHeight(node.left), getHeight(node.right))+1
        if root == None:
            return True
        if abs(getHeight(root.left)-getHeight(root.right))<=1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False