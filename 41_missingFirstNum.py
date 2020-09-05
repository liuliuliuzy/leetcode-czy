from typing import List
#非常数级别额外空间 O(n)
def firstMissingPositive(nums: List[int]) -> int:
    if not nums: return 1
    flags = [True for i in range(len(nums))]
    for item in nums:
        if item > 0 and item<=len(flags):
            flags[item-1] = False
    for i, flag in enumerate(flags):
        if flag: return i+1
    return len(flags)+1

#采用“-”号作为标记，在原数组基础上修改，这样空间复杂度就是O(1)了
def firstMissingPositiveV2(nums: List[int])->int:
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1
    
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    return n + 1

if __name__ == "__main__":
    x = [1, 2, 4, 6]
    print(firstMissingPositive(x))