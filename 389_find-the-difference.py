import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sd = collections.Counter(s)
        td = collections.Counter(t)
        ans = ''
        for key in td.keys():
            if key not in sd or td[key]-sd[key] == 1:
                ans = key
                break
            # print(key)
        return ans

if __name__ == "__main__":
    S = Solution()
    s = 'ada'
    t = 'daad'
    print(S.findTheDifference(s, t))