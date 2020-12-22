from typing import List
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        s1 = collections.deque()
        s2 = collections.deque()
        if not root: return ans
        s1.append(root)
        while s1 or s2:
            # from left to right
            if s1:
                tmp = []
                while s1:
                    n = s1.popleft()
                    tmp.append(n.val)
                    if n.left:
                        s2.append(n.left)
                    if n.right:
                        s2.append(n.right)
                ans.append(tmp)
            # from right to left
            else:
                tmp = []
                while s2:
                    n = s2.pop()
                    tmp.append(n.val)
                    if n.right:
                        s1.appendleft(n.right)
                    if n.left:
                        s1.appendleft(n.left)
                ans.append(tmp)
        return ans

if __name__ == "__main__":
    S = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(S.zigzagLevelOrder(root))