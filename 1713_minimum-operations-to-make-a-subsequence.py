from typing import List
import bisect

# 求最长公共子序列的长度
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        indexDict = {num: i for i, num in enumerate(target)}
        stacks = []
        # 接下来寻找arrs中的最长递增子序列
        for num in arr:
            if num in indexDict:
                index = indexDict[num]
                i = bisect.bisect_left(stacks, index)
                if i == len(stacks):
                    stacks.append(0)
                stacks[i] = index
        return len(target) - len(stacks)
