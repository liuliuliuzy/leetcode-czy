from typing import List
from collections import defaultdict as dt
from functools import reduce

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        遍历格子并且回溯
        md又是超时，/(ㄒoㄒ)/~~
        '''
        m, n = len(board), len(board[0])
        res = []
        visited = set()
        def backtrack(s: str, i: int, j: int):
            # 四个相邻的格子
            dis = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            if s in words and s not in res:
                res.append(s)
                # 不同return, 如果继续前进，可能还会找到想要的结果
                # return 
            for disI, disJ in dis:
                newI, newJ = disI + i, disJ + j
                # 第一层判断
                if 0 <= newI < m and 0 <= newJ < n and (newI, newJ) not in visited:
                    tmpFlag = False
                    for item in words:
                        if item.startswith(s+board[newI][newJ]):
                            tmpFlag = True
                            break
                    # 第二层判断
                    if tmpFlag:
                        visited.add((newI, newJ))
                        backtrack(s+board[newI][newJ], newI, newJ)
                        visited.remove((newI, newJ))
        
        for i in range(m):
            for j in range(n):
                visited.add((i, j))
                backtrack(board[i][j], i, j)
                visited.remove((i, j))
        
        return res

class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 初始化 行，列
        m,n = len(board),len(board[0])
        # 创建 trie树，根据官方的骚方法
        Tree = lambda: dt(Tree)
        tree = Tree()
        for w in words: reduce(dict.__getitem__,w+"#",tree)
        # 初始化返回的list和方向
        ret = []
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        # 深度搜索
        def dfs(used,x,y,dic,now):
            if "#" in dic: # 如果dic是末尾字符，即包含"#"字符
                ret.append(now) # 结算
                del dic["#"] # "某字符":{"#":{}} 中的key="#" 没了，"某字符" 的字典也空了
                
            used.add((x,y)) # 记录已访问过 board上的位置，避免这一次重复访问
            for direct in directions:
                # 四个方向 
                new_x = x + direct[0]
                new_y = y + direct[1]
                # 方向满足条件
                if 0 <= new_x < m and 0 <= new_y < n and (new_x,new_y) not in used:
                    # 检查这个新value是否在dic中
                    next_val = board[new_x][new_y]
                    if next_val in dic:
                        # 那么保存这个value，然后进入到对应这个value的字典
                        dfs(used,new_x,new_y,dic[next_val],now+next_val)
                        # 妙处，如果它里面没东西了，例如"#":{}已经被删除了。
                        # 那么它也没作用了
                        if not dic[next_val]: del dic[next_val]
            # 这一趟结束了，now已经存入ret，可以清除这个(x,y)
            used.remove((x,y))

        # 从每个节点开始
        for i in range(m):
            for j in range(n):
                curr_val = board[i][j]
                if curr_val in tree:
                    dfs(set(),i,j,tree[curr_val],curr_val)
                    if not tree[curr_val]: del tree[curr_val]

        return ret


if __name__ == "__main__":
    # board = [
    #     ["o","a","a","n"],
    #     ["e","t","b","e"],
    #     ["i","h","k","r"],
    #     ["i","f","l","v"]
    #     ]
    # words = ["oath","pea","eat","rain", "athk", "athkr"]
    # board = [["a"], ["a"], ["a"]]
    # words = ["aaa", "a", "aa"]
    board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
    words = ["lllllll","fffffff","ssss","s","rr","xxxx","ttt","eee","ppppppp","iiiiiiiii","xxxxxxxxxx","pppppp","xxxxxx","yy","jj","ccc","zzz","ffffffff","r","mmmmmmmmm","tttttttt","mm","ttttt","qqqqqqqqqq","z","aaaaaaaa","nnnnnnnnn","v","g","ddddddd","eeeeeeeee","aaaaaaa","ee","n","kkkkkkkkk","ff","qq","vvvvv","kkkk","e","nnn","ooo","kkkkk","o","ooooooo","jjj","lll","ssssssss","mmmm","qqqqq","gggggg","rrrrrrrrrr","iiii","bbbbbbbbb","aaaaaa","hhhh","qqq","zzzzzzzzz","xxxxxxxxx","ww","iiiiiii","pp","vvvvvvvvvv","eeeee","nnnnnnn","nnnnnn","nn","nnnnnnnn","wwwwwwww","vvvvvvvv","fffffffff","aaa","p","ddd","ppppppppp","fffff","aaaaaaaaa","oooooooo","jjjj","xxx","zz","hhhhh","uuuuu","f","ddddddddd","zzzzzz","cccccc","kkkkkk","bbbbbbbb","hhhhhhhhhh","uuuuuuu","cccccccccc","jjjjj","gg","ppp","ccccccccc","rrrrrr","c","cccccccc","yyyyy","uuuu","jjjjjjjj","bb","hhh","l","u","yyyyyy","vvv","mmm","ffffff","eeeeeee","qqqqqqq","zzzzzzzzzz","ggg","zzzzzzz","dddddddddd","jjjjjjj","bbbbb","ttttttt","dddddddd","wwwwwww","vvvvvv","iii","ttttttttt","ggggggg","xx","oooooo","cc","rrrr","qqqq","sssssss","oooo","lllllllll","ii","tttttttttt","uuuuuu","kkkkkkkk","wwwwwwwwww","pppppppppp","uuuuuuuu","yyyyyyy","cccc","ggggg","ddddd","llllllllll","tttt","pppppppp","rrrrrrr","nnnn","x","yyy","iiiiiiiiii","iiiiii","llll","nnnnnnnnnn","aaaaaaaaaa","eeeeeeeeee","m","uuu","rrrrrrrr","h","b","vvvvvvv","ll","vv","mmmmmmm","zzzzz","uu","ccccccc","xxxxxxx","ss","eeeeeeee","llllllll","eeee","y","ppppp","qqqqqq","mmmmmm","gggg","yyyyyyyyy","jjjjjj","rrrrr","a","bbbb","ssssss","sss","ooooo","ffffffffff","kkk","xxxxxxxx","wwwwwwwww","w","iiiiiiii","ffff","dddddd","bbbbbb","uuuuuuuuu","kkkkkkk","gggggggggg","qqqqqqqq","vvvvvvvvv","bbbbbbbbbb","nnnnn","tt","wwww","iiiii","hhhhhhh","zzzzzzzz","ssssssssss","j","fff","bbbbbbb","aaaa","mmmmmmmmmm","jjjjjjjjjj","sssss","yyyyyyyy","hh","q","rrrrrrrrr","mmmmmmmm","wwwww","www","rrr","lllll","uuuuuuuuuu","oo","jjjjjjjjj","dddd","pppp","hhhhhhhhh","kk","gggggggg","xxxxx","vvvv","d","qqqqqqqqq","dd","ggggggggg","t","yyyy","bbb","yyyyyyyyyy","tttttt","ccccc","aa","eeeeee","llllll","kkkkkkkkkk","sssssssss","i","hhhhhh","oooooooooo","wwwwww","ooooooooo","zzzz","k","hhhhhhhh","aaaaa","mmmmm"]

    s = Solution2()
    print(s.findWords(board, words))

    
