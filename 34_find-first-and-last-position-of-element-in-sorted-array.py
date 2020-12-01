from typing import List
import zyRandom

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (not nums) or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        def findLeft(left: int, right: int) -> int:
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid         
            return left
            
        def findRight(left: int, right: int) -> int:
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return right

        left, right = 0, len(nums) -1
        while left < right:
            # print(left, right)
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return [findLeft(left, mid), findRight(mid, right)]
        # print(left, right)
        if nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]


if __name__ == "__main__":
    S = Solution()
    # nums = zyRandom.createRandList(2, 10, 13)
    # nums.sort()
    nums = [2, 2]
    target = 2
    print(nums, target)
    print(S.searchRange(nums, target))
