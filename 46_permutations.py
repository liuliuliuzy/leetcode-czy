from typing import List
#回溯算法经典，全排列
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        #将当前索引作为回溯递归函数的参数
        def recursive(index):
            if index == n:
                ans.append(nums[:])
            for i in range(index, n):
                nums[index], nums[i] = nums[i], nums[index]
                recursive(index+1)
                nums[index], nums[i] = nums[i], nums[index]

        recursive(0)
        return ans
    def myHuisu(self, nums):
        n = len(nums)
        flags = [False for i in range(n)]
        def recursive(index, output):
            return


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 5, 6]
    print(s.permute(nums))