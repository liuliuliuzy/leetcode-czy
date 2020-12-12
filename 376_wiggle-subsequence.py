from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
        dynamic programming
        '''
        if len(nums) < 2:
            return  len(nums)
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] > nums[i-1]:
                up = down + 1
            else:
                down = up + 1

        return max(up, down)

    def wiggleMaxLengthII(self, nums: List[int]) -> int:
        '''
        greedy algorithm
        '''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        prevdiff = nums[1] - nums[0]
        ret = (2 if prevdiff != 0 else 1)
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff
        
        return ret    

if __name__ == "__main__":
    S = Solution()
    nums = [1,17,5,10,13,15,10,5,16,8]
    print(S.wiggleMaxLengthII(nums))