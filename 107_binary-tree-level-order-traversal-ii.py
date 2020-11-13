# Definition for a binary tree node.
from typing import List
import collections
class TreeNode:
    '''
    Definition of TreeNode
    '''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root == None:
            return res

        q = collections.deque()
        q.append(root)
        while q:
            tmpRes = []
            tmpNodeList = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                tmpRes.append(node.val)
                tmpNodeList.append(node)
            res.insert(0, tmpRes)
            for no in tmpNodeList:
                if no.left:
                    q.append(no.left)
                if no.right:
                    q.append(no.right)
        
        return res
            