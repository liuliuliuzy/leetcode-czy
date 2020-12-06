from typing import List
import collections

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        '''
        以下思路是错误的
        '''
        numbers = []
        maxTimes = 0
        counts = collections.defaultdict(int)
        for item in numbers:
            if item not in numbers:
                numbers.append(item)
            counts[item] += 1
            if counts[item] > maxTimes:
                maxTimes = counts[item]

        # counts = collections.Counter(nums)
        # maxTimes = counts.most_common(0)[1]

        for i in range(maxTimes):
            start = 0
            while start < len(counts):
                if counts[numbers[start]] == 0:
                    start += 1
                    continue
                tmpLen = 1
                while start < len(numbers) - 1 and numbers[start + 1] - numbers[start] == 1 and counts[numbers[start + 1]] > 0:
                    tmpLen += 1
                    start += 1
                if tmpLen < 3:
                    return False
        
        return True
    
    def isPossibleII(self, nums: List[int]) -> bool:
        

if __name__ == "__main__":
    S = Solution()
    nums = [1,2,3,3,4,5]
