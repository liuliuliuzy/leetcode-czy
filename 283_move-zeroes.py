from typing import List

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        对数组中全0段进行操作
        128ms 14.1Mb
        """
        start = 0
        while start < len(nums):
            if nums[start]:
                start += 1
                continue
            else:
                left = start
                zeroCount = 0
                while start < len(nums) and nums[start] == 0:
                    zeroCount += 1
                    start += 1
                if start == len(nums): break
                tmpIndex = start
                nonZeroCount = 0
                while tmpIndex < len(nums) and nums[tmpIndex]:
                    nonZeroCount += 1
                    tmpIndex += 1
                print(zeroCount, nonZeroCount)
                for i in range(nonZeroCount):
                    nums[left + i] = nums[left + i + zeroCount]
                for j in range(zeroCount):
                    nums[tmpIndex - 1 - j] = 0
                start = tmpIndex - zeroCount
    
    def moveZeroesMuchBetter(self, nums: List[int]) -> None:
        '''
        44ms 14.1Mb
        '''
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1
    
    def moveZeroesOneLine(self, nums: List[int]) -> None:
        '''
        36ms 14.2Mb
        '''
        nums.sort(key = lambda x: x == 0)


if __name__ == "__main__":
    nums = [1,2,3,4,0,4]
    s = Solution()
    s.moveZeroesMuchBetter(nums)
    print(nums)