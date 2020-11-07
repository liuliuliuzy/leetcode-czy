from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 遍历回溯
        p = 0 # 字符串字符指针
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != word[p]:
                    continue
                # 执行回溯算法
                for t in range
                for disI, disJ in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                    p += 1
                    if i+disI >= 0 and i+disI < n and j+disJ >= 0 and j+disJ < n and board[i][j] == word[p]:


        return False

if __name__ == "__main__":
    board =[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    s = "ABC"
    solu = Solution()
    solu.exist(board, s)

    
