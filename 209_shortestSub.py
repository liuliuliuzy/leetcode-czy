import bisect
#为了能够指定参数类型为List[int]
from typing import List

#自己写的滑动窗口
def minSubArrayLen(s: int, nums) -> int:
    res = len(nums)+1
    left = 0
    right = 1

    #特殊情况
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        if nums[0] >= s:
            return 1
        else:
            return 0
    tmpSum = nums[0]
    while left < right:
        while tmpSum < s and right < len(nums):
            tmpSum += nums[right]
            right += 1
        if right == len(nums) and left == 0 and tmpSum < s:
            return 0
        if tmpSum >= s: res = min(right-left, res)
        #如果可以到1，那么1肯定是最小长度
        if res == 1: return res
        tmpSum -= nums[left]
        left += 1
        while tmpSum >= s:
            res = min(right-left, res) 
            tmpSum -= nums[left]
            left += 1      
        if right == len(nums):
            break
    return res

def minSubArrayLenBi(s: int, nums: List[int]) -> int:
    if not nums:
        return 0
    
    n = len(nums)
    ans = n + 1
    sums = [0]
    for i in range(n):
        sums.append(sums[-1] + nums[i])
    
    for i in range(1, n + 1):
        target = s + sums[i - 1]
        bound = bisect.bisect_left(sums, target)
        if bound != len(sums):
            ans = min(ans, bound - (i - 1))
    
    return 0 if ans == n + 1 else ans

#题解中的标准滑动窗口
def minSubArrayLenSlidingWin(s: int, nums: List[int])->int:
    if not nums:
        return 0
    
    n = len(nums)
    ans = n + 1
    start, end = 0, 0
    total = 0
    while end < n:
        total += nums[end]
        while total >= s:
            ans = min(ans, end - start + 1)
            total -= nums[start]
            start += 1
        end += 1
    
    return 0 if ans == n + 1 else ans

if __name__ == "__main__":
    target = 5
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLenBi(target, nums))