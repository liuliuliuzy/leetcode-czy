from typing import List
# 回溯＋剪枝


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 首先对待选元素进行排序
        nums.sort()
        ans = []
        n = len(nums)

        def rec(index=0):
            if index == n:
                ans.append(nums[:])
            for i in range(index, n):
                # 剪枝
                if nums[i] != nums[index]:
                    nums[index], nums[i] = nums[i], nums[index]
                    rec(index + 1)
                    nums[index], nums[i] = nums[i], nums[index]
        rec()
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 2, 3]
    print(s.permuteUnique(nums))
