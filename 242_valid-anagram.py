import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdt = collections.defaultdict(int)
        tdt = collections.defaultdict(int)
        for i in range(len(s)):
            sdt[s[i]] += 1
            tdt[t[i]] += 1

        return sdt == tdt


if __name__ == "__main__":
    s = Solution()
    x1 = "a你agrbm"
    x2 = "你agarbm"
    print(s.isAnagram(s=x1, t=x2))