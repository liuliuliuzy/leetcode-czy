from typing import List

# 动态规划
def findLength(A: List[int], B: List[int]) -> int:
    dp = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
    res = 0
    # commonArray = []
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
            res = max(res, dp[i][j])
    #         if res < dp[i][j]:
    #             commonArray = A[i:i+dp[i][j]]
    #             res = dp[i][j]
    # print(commonArray)
    return res

# 滑动窗口
def findLengthV2(A: List[int], B: List[int]) -> int:
    

if __name__ == "__main__":
    a = [1,2,3,2,1]
    b = [3,2,1,4,7]
    print(findLength(a, b))