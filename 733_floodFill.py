from typing import List
import queue
class Solution:
    # DFS, 通过递归就能非常简单地完成矩阵的深度优先搜索
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i, j, originColor):
            if 0<=i<len(image) and 0<=j<len(image[0]) and image[i][j]==originColor:
                image[i][j] = newColor
                dfs(i-1, j, originColor)
                dfs(i+1, j, originColor)
                dfs(i, j-1, originColor)
                dfs(i, j+1, originColor)
        
        if image[sr][sc] != newColor:
            dfs(sr, sc, image[sr][sc])
        
        return image
    
    # BFS，使用队列完成
    def floodFillBfs(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc]!=newColor:
            q = queue.Queue()
            base = image[sr][sc]
            image[sr][sc] = newColor
            q.put((sr, sc))
            while not q.empty():
                i, j = q.get()
                if 0<=i-1 and image[i-1][j]==base:
                    image[i-1][j] = newColor
                    q.put((i-1,j))
                if i+1<len(image) and image[i+1][j]==base:
                    image[i+1][j] = newColor
                    q.put((i+1,j))
                if 0<=j-1 and image[i][j-1]==base:
                    image[i][j-1] = newColor
                    q.put((i,j-1))
                if j+1<len(image[0]) and image[i][j+1]==base:
                    image[i][j+1] = newColor
                    q.put((i,j+1))
        return image

# python的三元表达式：h = a-b if a>b else a+b (只是举个例子)


if __name__ == "__main__":
    # testImg = [[0, 0, 0], [1, 0, 0]]
    testImg = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    solu = Solution()
    print(testImg)
    solu.floodFillBfs(testImg, 1, 1, 2)
    print(testImg)

                
