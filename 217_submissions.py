from typing import List
import collections

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dt = collections.defaultdict(int)
        for item in nums:
            dt[item] += 1
            if dt[item] > 1:
                return True
        return False