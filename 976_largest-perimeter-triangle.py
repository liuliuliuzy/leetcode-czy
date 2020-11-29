from typing import List

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        '''
        提高了时间复杂度，不用两个for嵌套的
        '''
        # 从大到小排序
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            for j in range(i+1, len(A) - 1):
                if A[i] - A[j] < A[j+1]:
                    return (A[i] + A[j] + A[j+1])
                else:
                    continue
        return 0

    def largestPerimeterII(self, A: List[int]) -> int:
        '''
        排序后的紧靠着的三个元素每次都是最可能的选择，所以只需要一个for循环
        '''
        A.sort(key=lambda x: -1*x)
        for i in range(len(A) - 2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
        
if __name__ == "__main__":
    s = Solution()
    sides = [2,1,2,3,4,5,6,7,8,14]
    print(s.largestPerimeterII(sides))