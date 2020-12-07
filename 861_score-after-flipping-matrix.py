from typing import List

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        '''
        贪心
        看了题解思路然后最直接的实现
        '''
        def reverseRow(i: int):
            if 0 <= i < m:
                for j in range(n):
                    A[i][j] = 1 - A[i][j]
        
        def reverseCol(j: int):
            if 0 <= j < n:
                for i in range(m):
                    A[i][j] = 1 - A[i][j]

        def calcuSum() -> int:
            res = 0
            for i in range(m):
                res += int("".join([str(A[i][j]) for j in range(n)]), 2)
            return res

        m, n = len(A), len(A[0])
        for i in range(m):
            if A[i][0] == 1:
                continue
            reverseRow(i)
        
        for j in range(n):
            onesCount = 0
            for i in range(m):
                if A[i][j] == 0:
                    onesCount += 1
            if onesCount > m//2:
                reverseCol(j)
        
        return calcuSum()

    def matrixScoreII(self, A: List[List[int]]) -> int:
        '''
        按照贪心的反转策略，直接计算元素贡献
        '''
        m, n = len(A), len(A[0])
        ans = (1 << (n - 1))*m
        for j in range(1, n):
            onesCount = 0
            for i in range(m):
                if A[i][0] ^ A[i][j]:
                    continue
                onesCount += 1
            ans += max(onesCount, m-onesCount)*(1 << (n - 1 - j))
        
        return ans




if __name__ == "__main__":
    S = Solution()
    A = [
        [0,1,0,1,1],
        [1,1,1,1,0],
        [1,0,1,0,1]
    ]
    print(S.matrixScore(A))
    print(A)