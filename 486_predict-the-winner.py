from typing import List
import math

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def maxScores(nums, isFirst):
            if(len(nums) == 1):
                if(isFirst):
                    return nums[0]
                else:
                    return 0
            # 先取
            if(isFirst):
                return max(nums[0]+maxScores(nums[1:], False), nums[-1]+maxScores(nums[:-1], False))
            # 后取
            else:
                return max(maxScores(nums[1:], True), maxScores(nums[:-1], True))
        print(maxScores(nums, True), maxScores(nums, False))
        return maxScores(nums, True)>maxScores(nums, False)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 5,2]
    print(s.PredictTheWinner(nums))
