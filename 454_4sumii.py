from typing import List
import collections

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        '''
        哈希表
        二分查找
        将ABCD分为AB和CD两组数组，确实是非常有效的一种思路，考虑到4这个数字的特殊性
        '''
        N = len(A)
        if not N: return 0
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        if (A[0] + B[0] + C[0] + D[0]) > 0 or (A[-1] + B[-1] + C[-1] + D[-1]) < 0:
            return 0
        
        res = 0
        sumDt = collections.defaultdict(int)
        for i in range(N):
            for j in range(N):
                target = A[i] + B[j]
                sumDt[target] += 1
        
        for k in range(N):
            for l in range(N):
                target2 = -1 * (C[k] + D[l])
                res += sumDt[target2]

        return res

if __name__ == "__main__":
    s = Solution()
    a = []
    b = []
    c = []
    d = []
    print(s.fourSumCount(a, b, c, d))

