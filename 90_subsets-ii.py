from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        回溯算法yyds
        '''
        res = []
        path = []
        n = len(nums)
        def backtrack(path: List[int], i: int):
            if path not in res:
                res.append(path[:])
            for j in range(i, n):
                path.append(nums[j])
                backtrack(path, j+1)
                path.pop()

        def quickSort(start: int, end: int):
            if start < end:
                i = start
                j = end
                pivot = nums[i]
                while i < j:
                    while i < j and nums[j] >= pivot:
                        j -= 1
                    if i < j:
                        nums[i] = nums[j]
                        i += 1
                    while i < j and nums[i] <= pivot:
                        i += 1
                    if i < j:
                        nums[j] = nums[i]
                        j -=1
                
                nums[i] = pivot
                quickSort(start, i-1)
                quickSort(i+1, end)

        # 为了能够正确判断 path not in res，需要对nums进行排序
        quickSort(0, n - 1)
        backtrack(path, 0)
        return res

if __name__ == "__main__":
    testNums = [4, 1, 5, 8, 2, 2, 3, 3, 4]
    s = Solution()
    print(s.subsetsWithDup(testNums))
    
