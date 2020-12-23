class Solution:
    def firstUniqChar(self, s: str) -> int:
        dt = {}
        seen = []
        sigSeen = []
        for i, char in enumerate(s):
            if char not in seen:
                seen.append(char)
                dt[char] = i
                sigSeen.append(char)
            else:
                # print(char)
                if char in sigSeen:
                    sigSeen.remove(char)
        
        if sigSeen:
            return dt[sigSeen[0]]
        else:
            return -1
    
    def firstUniqCharII(self, s:str) -> int:
        dt = [0 for i in range(26)]
        res = 0
        for i in range(len(s)):
            dt[ord(s[i]) - 0x61] += 1
            while res <= i and dt[ord(s[res]) - 0x61] > 1:
                res += 1
        
        if res == len(s):
            return -1
        else:
            return res


if __name__ == "__main__":
    s = 'degfwefdqwfrgqr'
    S = Solution()
    print(S.firstUniqCharII(s))
