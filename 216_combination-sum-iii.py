from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        找出所有的k个1~9之间的且和为n的所有数字组合
        组合中不含有重复数字
        '''
        res = []
        path = []
        def backtrack(start: int, Sum: int):
            if len(path) == k:
                if Sum == n:
                    res.append(path[:])
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(i+1, Sum+i)
                path.pop()
        
        backtrack(1, 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(6, 35))
