from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        '''
        O(n) 可以做
        '''
        # 偶数后缀和
        evenSum = 0
        evenSums = [0]
        # 奇数后缀和
        oddSum = 0
        oddSums = [0]
        res = 0
        for i in range(len(nums)-1, -1, -1):
            if i % 2 == 0:
                evenSum += nums[i]
                evenSums.insert(0, evenSum)
            else:
                oddSum += nums[i]
                oddSums.insert(0, oddSum)

        for j in range(len(nums)):
            if j % 2 == 0:
                if evenSums[0] - evenSums[j//2] + oddSums[j//2] == oddSums[0] - oddSums[j//2] + evenSums[j//2+1]:
                    res += 1
            else:
                if oddSums[0] - oddSums[j//2] + evenSums[j//2+1] == evenSums[0] - evenSums[j//2+1] + oddSums[j//2+1]:
                    res += 1
        return res

if __name__ == "__main__":
    s = [1,2,3,4,5,6,4]
    S = Solution()
    print(S.waysToMakeFair(s))