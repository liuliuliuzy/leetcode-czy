from typing import List

# DP, O(mn)
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1: return 0
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if m ==1 and n == 1: return 1
    fMat = [[(0, 0) for i in range(n)] for j in range(m)]
    for i in range(m-1):
        if obstacleGrid[i+1][0] == 0:
            fMat[i+1][0] = (1, 1)
        else:
            break
    for j in range(n-1):
        if obstacleGrid[0][j+1] == 0:
            fMat[0][j+1] = (1, 1)
        else:
            break
    for i in range(m-1):
        for j in range(n-1):
            if obstacleGrid[i+1][j+1] == 0:

                fMat[i+1][j+1] = (fMat[i][j+1][0] + fMat[i+1][j][0], 1)
    return fMat[m-1][n-1][0]

if __name__ == "__main__":
    x = [
        [0,0],
        [1,1],
        [0,0]
        ]
    print(uniquePathsWithObstacles(x))