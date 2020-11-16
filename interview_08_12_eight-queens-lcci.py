from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
        输入N
        输出N皇后的所有不同解法
        回溯
        '''
        res = []
        # used = [[0 for i in range(n)] for j in range(n)]
        used = [0 for i in range(n)]
        path = []

        def backtrack(path: List[str], count: int):
            if count == n:
                res.append(path[:])
            for i in range(n):
                # if used[i]:
                #     continue

                flag = True
                for a1 in range(count):
                    if path[a1][i] == 'Q' or (i-count+a1 >= 0 and path[a1][i-count+a1] == 'Q') or (i+count-a1 < n and path[a1][i+count-a1] == 'Q'):
                        flag = False
                        break
                if not flag:
                    continue
                path.append("."*(i)+"Q"+"."*(n-1-i))
                # used[i] = 1
                backtrack(path, count+1)
                path.pop()
                # used[i] = 0
            
        backtrack(path, 0)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))
