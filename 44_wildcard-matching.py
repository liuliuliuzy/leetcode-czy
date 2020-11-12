class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        超时了，我艹
        '''
        if not p:
            return not s
        if not s:
            if len(p) <= 1:
                return not p or  p=='*'
            else:
                for chara in p:
                    if chara != '*':
                        return False
                return True
        
        if p[0] == '*':
            for i in range(len(s)+1):
                if self.isMatch(s[i:], p[1:]):
                    return True
            return False
        else:
            firstMatch = p[0] in [s[0], '?']

            return firstMatch and self.isMatch(s[1:], p[1:])

class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        很好，继续超时 :-()，需要优化p中很多个*的情况
        '''
        result = False
        n1 = len(s)
        n2 = len(p)
        def backtrack(si: int, pi: int):
            nonlocal result
            # 终止条件
            if pi == n2:
                result = (si == n1)
                return
            
            if p[pi] != '*':
                # FIXME: 这里有点问题
                if si >= n1:
                    return
                else:
                    if p[pi] == '?' or s[si] == p[pi]:
                        backtrack(si+1, pi+1)
                    else:
                        return
            else:
                if pi+1 < n2 and p[pi+1] == '*':
                    backtrack(si, pi+1)
                else:
                    for i in range(si, n1+1):
                        backtrack(i, pi+1)
                        if result:
                            break
        if not s:
            for chara in p:
                if chara != '*':
                    return False
            return True

        backtrack(0, 0)
        return result

class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        动态规划
        '''
        n1 = len(s)
        n2 = len(p)
        dp = [[False for j in range(n2 + 1)] for i in range(n1 + 1)]
        dp[0][0] = True
        for i in range(n2):
            if p[i] != '*':
                break
            dp[0][i+1] = True

        for i in range(n1):
            for j in range(n2):
                if p[j] == '?' or s[i] == p[j]:
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    dp[i+1][j+1] = dp[i][j+1] | dp[i][j+1]
                    # 就因为这里的下标写错了一直没看出来，导致我提交错误了3次🤬...
                else:
                    continue

        return dp[n1][n2]

    def isMatch2(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        print(dp)
        return dp[m][n]

if __name__ == "__main__":
    s = "abceb"
    p = "a*b"
    S = Solution3()
    print(S.isMatch(s, p))
    