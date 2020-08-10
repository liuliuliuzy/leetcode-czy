class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        count = count_another = 0
        for i in range(len(s)):
            count_another = count_another + 1
            if(i<len(s)-1 and s[i+1]!=s[i]):
                ans = ans + min(count, count_another)
                count = count_another
                count_another = 0
        ans = ans + min(count,count_another)
        return ans