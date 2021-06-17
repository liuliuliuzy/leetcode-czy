from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums:
            return ans
        nums.sort()
        last = nums[0]
        tmp = str(last)
        i = 1
        while i < len(nums):
            if nums[i] == last + 1:
                while i < len(nums) and nums[i] == last + 1:
                    last = nums[i]
                    i += 1
                tmp += ('->' + str(last))
                if i < len(nums):
                    last = nums[i]
            else:
                ans.append(tmp)
                last = nums[i]
                tmp = str(last)
                i += 1
        ans.append(tmp)
        return ans


if __name__ == "__main__":
    S = Solution()
    nums = [1, 4, 5, 8, 6, 9]
    print(S.summaryRanges(nums))
