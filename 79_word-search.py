from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 四个方向
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def judge(i: int, j: int, k: int) -> bool:
            # 如果不等，则不可能匹配成功
            if board[i][j] != word[k]:
                return False

            # 如果已经匹配完了最后一个字符
            if k == len(word)-1:
                return True
            
            result = False
            visited.add((i, j))
            for di, dj in directions:
                newi, newj = i+di, j+dj
                if 0 <= newi < m and 0 <= newj < n:
                    # 如果没被访问过
                    if (newi, newj) not in visited:
                        if judge(newi, newj, k+1):
                            result = True
                            break
            
            visited.remove((i, j))
            return result            

        # 遍历回溯
        # p = 0 # 字符串字符指针
        m = len(board)
        n = len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if judge(i, j, 0):
                    return True
        return False

if __name__ == "__main__":
    board =[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    s = "ABCCED"
    solu = Solution()
    print(solu.exist(board, s))

    
