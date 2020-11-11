from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        回溯算法
        '''
        n1 = len(s)
        n2 = len(p)
        def backtrack(pStart: int, sStart: int):
            if pStart == n2 and sStart = n1:
                return True
            result = False
            # if (p[pStart] != '*' or p[pStart] != '.') and (pStart < n2-1 and p[pStart+1] != '*')
            # 可以匹配0个或多个字符
            
            # 只能匹配一个字符
            if pStart < n2-1 and p[pStart+1] != '*':
                if p[pStart] == '.':
                    if backtrack(pStart+1, sStart+1):
                        return True