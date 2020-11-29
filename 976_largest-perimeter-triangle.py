from typing import List

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # 从大到小排序
        A.sort(reverse=True)
        
        return 0

if __name__ == "__main__":
    s = Solution()
    sides = []
    print(s.largestPerimeter(sides))