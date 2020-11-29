from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> List[int]:
        '''
        数组中每对数字和在经过修改之后，能够到达[2, 2*limit]区间内每一个数
        但是到达不同数所需要的修改次数不同
        我们遍历每对数字和，再对[2, 2*limit]中的每个数字加上这对数字和所贡献的修改次数
        最后，[2, 2*limit]中对应修改次数最小的值即为所求结果

        learned: 对于数组区间中每个元素都加上一个值，可以通过对区间端点操作来实现（前提是数组的初始值为0）
        '''
        B = [0 for i in range(2*limit+2)]
        for i in range(len(nums)//2):
            # sums = nums[i] + nums[len(nums) - 1 - i]
            a = max(nums[i], nums[len(nums) - 1 - i])
            b = min(nums[i], nums[len(nums) - 1 - i])
            B[2] += 2
            B[b + 1] -= 1
            # B[b + 1] += 1
            B[a + b] -= 1
            B[a + b + 1] += 1
            # B[a + limit + 1] -= 1
            B[a + limit + 1] += 1
            B[2*limit + 1] += -2
        res = len(nums)+1
        for j in range(2, 2*limit + 1):
            B[j] += B[j - 1]
            res = min(B[j], res)
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,2,1]
    print(s.minMoves(nums, 2))     