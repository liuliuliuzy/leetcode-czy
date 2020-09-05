class Solution:
    # 很不幸，这个解答超时了...
    def longestPalindrome_outTime(self, s: str) -> str:
        if len(s) <= 1:
            return s
        ans =  s[0]
        for i in range(1, len(s)):
            tmpAns = ''
            for j in range(i-1, -1, -1):
                if s[j:i+1][::-1] == s[j:i+1]:
                    tmpAns = s[j:i+1]
            print("'", tmpAns, "'")
            if tmpAns:
                if len(tmpAns)>len(ans):
                    ans = tmpAns  
        return ans
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for k in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + k
                if j >= len(s):
                    break
                if k == 0:
                    dp[i][j] = True
                elif k == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and k + 1 > len(ans):
                    ans = s[i:j+1]
        return ans


if __name__ == "__main__":
    s = 'ababs'
    x = Solution()
    print(x.longestPalindrome(s))