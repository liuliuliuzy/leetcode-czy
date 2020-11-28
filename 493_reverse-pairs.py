from typing import List
import time
import random

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        '''
        思路：
        遍历肯定是不行的，O(n^2)会超时
        题解思路：归并排序
        接下来使用Python自己实现
        明明是nlogn啊为什么会超时呢
        '''

        def myMerge(left: int, right: int) -> int:
            if left == right:
                return 0
            res = 0
            mid = (left + right) // 2
            n1 = myMerge(left, mid)
            n2 = myMerge(mid + 1, right)
            res += (n1 + n2)
            # 计算i在左，j在右的数量
            for i in range(left, mid + 1):
                j = mid + 1
                while (j < right + 1) and (2 * nums[j]) < nums[i]:
                    res += 1
                    j += 1

            # 归并
            merged = [0 for i in range(right - left + 1)]
            i = left
            j = mid + 1
            k = 0
            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    merged[k] = nums[i]
                    i += 1
                else:
                    merged[k] = nums[j] 
                    j += 1
                k += 1
            if i == mid + 1:
                while j <= right:
                    merged[k] = nums[j]
                    j += 1
                    k += 1
            else:
                while i <= mid:
                    merged[k] = nums[i]
                    i += 1
                    k += 1
            for t in range(left, right + 1):
                nums[t] = merged[t - left]
            return res
        
        if not nums:
            return 0
        return myMerge(0, len(nums) - 1)

    def reversePairsII(self, nums: List[int]) -> int:
        '''
        这样就不超时了
        但是还是很慢🙄
        '''
        def countPairs(left: int, mid: int, right: int) -> int:
            res = 0
            lastj = mid + 1
            # 由于左右两边是已经排好序的，所以这里可以优化，对第一个之后的i，j并不需要从头开始遍历
            for i in range(left, mid + 1):
                while lastj <= right and nums[i] > 2 * nums[lastj]:
                    lastj += 1
                res += lastj - (mid + 1)
            return res
        
        def mergeAndCount(left: int, right: int) -> int:
            if left == right: return 0
            mid = (left + right) // 2
            res = mergeAndCount(left, mid) + mergeAndCount(mid + 1, right) + countPairs(left, mid, right)
            i,j,k = left, mid+1, left
            while i < mid+1 and j < right+1:
                if nums[i] < nums[j]: 
                    sortedNums[k] = nums[i]
                    i += 1
                else:
                    sortedNums[k] = nums[j]
                    j += 1
                k += 1
            
            while i < mid+1:
                sortedNums[k] = nums[i]
                i += 1
                k += 1

            while j < right+1:
                sortedNums[k] = nums[j]
                j += 1
                k += 1
            
            for t in range(left, right+1):
                nums[t] = sortedNums[t]
            
            return res

        if not nums:
            return 0
        sortedNums = [0 for i in range(len(nums))]
        return mergeAndCount(0, len(nums)-1)
                
if __name__ == "__main__":
    s = Solution()
    nums = [1, 26, 20, 66, 28, 75, 78, 15, 40, 64]
    # random.seed(time.time())
    # for i in range(10):
    #     nums.append(random.randrange(1,100))
    print(nums)
    print(s.reversePairs(nums))
    print(nums)
            