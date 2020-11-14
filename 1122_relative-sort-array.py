from typing import List
from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        '''
        两个数组存储结果，然后拼接
        '''
        dt = defaultdict(int)
        for index, item in enumerate(arr2):
            dt[item] = index
        
        res = []
        res2 = []
        for num in arr1:
            if num in arr2:
                j = 0
                while j < len(res) and dt[res[j]] <= dt[num]:
                    j += 1
                res.insert(j, num)
            else:
                i = 0
                while i < len(res2) and res2[i] <= num:
                    i += 1
                res2.insert(i, num)
        
        res.extend(res2)
        return res
    
    def relativeSortArrayII(self, arr1: List[int], arr2: List[int]) -> List[int]:
        '''
        python可以对元组进行比较大小操作
        sort内置排序函数可以传入key参数，自定义比较方法
        于是就有以下的python式解法
        '''
        dt = {x: i for i, x in enumerate(arr2)}
        def myKey(x: int) -> (int, int):
            if x in arr2:
                return (0, dt[x])
            else:
                return (1, x)
        
        arr1.sort(key=myKey)
        return arr1

if __name__ == "__main__":
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [3,1,7]
    s = Solution()
    print(s.relativeSortArrayII(arr1, arr2))        