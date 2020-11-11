from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        回溯算法

        如何用回溯算法来完成 . 和 * 的正则表达式匹配？
        '''
        if not p: return not s
        # 第一个字母是否匹配
        first_match = bool(s and p[0] in {s[0],'.'})
        # 如果 p 第二个字母是 *
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or \
            first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

        