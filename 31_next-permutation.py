from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = False
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                # print(i, nums)
                for j in range(n-1, i-1, -1):
                    if nums[j] <= nums[i-1]:
                        continue
                    else:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                for j in range((n-i)//2):
                    nums[i+j], nums[n-1-j] = nums[n-1-j], nums[i+j]
                flag = True
                break
        if not flag:
            for i in range(n//2):
                nums[i], nums[-1*i-1] = nums[-1*i-1], nums[i]
    
    def nextPermutationSimple(self, nums: List[int]) -> None:
        n = len(nums)
        start = n - 1
        while start > 0:
            if nums[start] <= nums[start - 1]:
                start -= 1
                continue
            for j in range(n-1, start-1, -1):
                if nums[j] > nums[start - 1]:
                    nums[j], nums[start - 1] = nums[start - 1], nums[j]
                    break
            break
        for i in range((n - start) // 2):
            nums[start + i], nums[n - 1 - i] = nums[n - 1 - i], nums[start + i]

if __name__ == "__main__":
    nums = [3,5,1,2,4]
    s = Solution()
    s.nextPermutationSimple(nums)
    print(nums)