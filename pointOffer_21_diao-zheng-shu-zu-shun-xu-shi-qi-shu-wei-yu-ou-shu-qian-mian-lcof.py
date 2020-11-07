from typing import List

class Solution:
    # 不考虑空间的话是不是刷流氓😂
    def exchange(self, nums: List[int]) -> List[int]:
        oddNums = []
        evenNums = []
        for item in nums:
            if item%2:
                oddNums.append(item)
            else:
                evenNums.append(item)
        return oddNums+evenNums
    
    # 双指针
    def exchangeV2(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        while left < right:
            while left < right and nums[left]%2:
                left += 1
            while right > left and not nums[right]%2:
                right -= 1
            print(left, right)
            nums[left], nums[right] = nums[right], nums[left]
        return nums

if __name__ == "__main__":
    nums = [2, 21, 1231, 14, 343]
    s= Solution()
    print(s.exchangeV2(nums))