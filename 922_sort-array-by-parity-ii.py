from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        '''
        找到第一个不合格的偶数和第一个不合格的奇数，然后交换
        '''
        oddIndex = 1
        evenIndex = 0
        n = len(A)
        while oddIndex < n and evenIndex < n:
            while evenIndex < n-1 and  A[evenIndex] % 2 == 0:
                evenIndex += 2
            while oddIndex < n and A[oddIndex] % 2 == 1:
                oddIndex += 2
            if evenIndex < n - 1 and oddIndex < n:
                A[evenIndex], A[oddIndex] = A[oddIndex], A[evenIndex]
            evenIndex += 2
            oddIndex += 2
        return A


if __name__ == "__main__":
    s = Solution()
    A = [2, 3, 3, 2]
    print(s.sortArrayByParityII(A))
    
        