from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
        贪心算法
        '''
        # m = len(nums)
        # if m < 3:
        #     return m
        # res = [nums[0]]
        # flag = 0
        # for i in range(1, len(nums)):
        #     if nums[i] == res[-1]:
        #         continue
        #     if flag == 0:
        #         res.append(nums[i])
        #         flag = 1 if res[-1] > res[-2] else -1
        #     else:
        #         if flag == 1:
        #             if nums[i] > res[-1]:
        #                 res[-1] = nums[i]
        #             else:
        #                 res.append(nums[i])
        #         else:
        #             if nums[i] < res[-1]:
        #                 res[-1] = nums[i]
        #             else:
        #                 res.append(nums[i])
        
        # return len(res)
        up ,down = 1,1
        if len(nums)<2:return len(nums)
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                up = down+1
            if nums[i]<nums[i-1]:
                down = up+1
        return max(up,down)

if __name__ == "__main__":
    S = Solution()
    nums = [1,17,5,10,13,15,10,5,16,8]
    print(S.wiggleMaxLength(nums))