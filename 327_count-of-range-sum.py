from typing import List
import random
import time

# 最容易理解的思路：前缀和
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def countRec(lower: int, upper: int, left: int, right: int) -> int:
            if left == right:
                return 0
            # n1 n2 分别代表左半边和右半边前缀和数组中存在的符合条件的下标对数
            n1 = countRec(lower, upper, left, (left+right)//2)
            n2 = countRec(lower, upper, (left+right)//2+1, right)
            res = n1+n2

            # 接下来计算一个下标在左数组，一个下标在右数组的对数
            i = left
            L = R = (left+right)//2+1
            # 移动L与R
            while i <= (left+right)//2:
                while L<=right and sums[L]-sums[i] < lower:
                    L+=1
                while R<=right and sums[R]-sums[i] <= upper:
                    R+=1
                res += (R-L)
                i += 1
            # 为了保证左右数组的有序性，需要在这里进行归并排序
            # 创建临时数组
            sortedNums = []
            p1 = left
            p2 = (left+right)//2+1
            while p1 <= (left+right)//2 or p2 <= right:
                if p1 > (left+right)//2:
                    while p2 <= right:
                        sortedNums.append(sums[p2])
                        p2+=1
                elif p2 > right:
                    while p1 <= (left+right)//2:
                        sortedNums.append(sums[p1])
                        p1+=1
                else:
                    if sums[p1] < sums[p2]:
                        sortedNums.append(sums[p1])
                        p1+=1
                    else:
                        sortedNums.append(sums[p2])
                        p2+=1
            # 修改待排序数组
            for i in range(len(sortedNums)):
                sums[left+i] = sortedNums[i]

            return res
        # 首先计算前缀和数组
        sums = [0]
        for item in nums:
            sums.append(sums[-1]+item)

        return countRec(lower, upper, 0, len(nums))

    def mergeSort(self, nums: List[int], left: int, right: int) -> List[int]:
        if right - left <= 1:
            return nums[left: right+1]
        leftNums = self.mergeSort(nums, left, (left+right)//2)
        rightNums = self.mergeSort(nums, (left+right)//2+1, right)

        # 合并
        newSums = []
        i = j = 0
        while i<len(leftNums) and j<len(rightNums):
            if leftNums[i]<rightNums[j]:
                newSums.append(leftNums[i])
                i+=1
            else:
                newSums.append(rightNums[j])
                j+=1
        while i<len(leftNums):
            newSums.append(leftNums[i])
            i+=1
        while j<len(rightNums):
            newSums.append(rightNums[j])
            j+=1
        return newSums

if __name__ == "__main__":
    testNums = []
    random.seed(time.time())
    for i in range(10):
        testNums.append(random.randrange(-10, 10))
    testNums = [-2, 5, -1]
    lower = -2
    upper = 2
    s = Solution()
    # print(s.mergeSort(testNums, 0, len(testNums)))
    print(testNums)
    print(s.countRangeSum(testNums, lower, upper))
