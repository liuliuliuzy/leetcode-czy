from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        '''
        贪心算法
        超时gg
        '''
        if k == len(nums):
            return nums

        tmpK = k
        n = len(nums)
        left = 0
        res = []
        while tmpK > 0:
            tmp = nums[left]
            i = left
            tmpIndex = left
            while i < n-tmpK+1:
                if nums[i] < tmp:
                    tmp = nums[i]
                    tmpIndex = i
                i += 1
            res.append(tmp)
            left = tmpIndex + 1
            tmpK -= 1
        return res
    
    def mostCompetitiveII(self, nums: List[int], k: int) -> List[int]:
        '''
        DP?
        '''
        

if __name__ == "__main__":
    s = Solution()
    nums = [3,5,2,6,1,3,4,2]
    print(s.mostCompetitive(nums, 2))