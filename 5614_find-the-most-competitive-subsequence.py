from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        '''
        贪心算法
        复杂度应该是O(nk)
        超时gg /(ㄒoㄒ)/~~
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
        DP? no no no
        单调栈
        '''
        monoStack = [nums[0]]
        for i in range(1, len(nums)):
            # 还有选择的余地
            if len(nums) - i > k - len(monoStack):
                while monoStack and monoStack[-1] > nums[i] and len(nums) - i > k - len(monoStack):
                    monoStack.pop()
                if len(monoStack) < k:
                    monoStack.append(nums[i])
            # 没有选择的余地了
            else:
                monoStack.extend(nums[i:])
                break
        
        return monoStack


if __name__ == "__main__":
    s = Solution()
    nums = [3,5,2,6,1,3,4,5]
    print(s.mostCompetitiveII(nums, 1))