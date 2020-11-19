from typing import List

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        别说了，递归又超时了。。。
        '''
        res = 0
        ress = []
        tmp = []
        n1, n2 = len(s), len(t)
        def dfs(path: List[int], start: int, nowIndex: int):
            nonlocal res
            if n1 - start < n2 - nowIndex:
                return
            if nowIndex == n2:
                ress.append(path[:])
                res += 1
                return
            dfs(path[:], start+1, nowIndex)
            if s[start] == t[nowIndex]:
                path.append(start)
                dfs(path[:], start+1, nowIndex+1)

        dfs(tmp, 0, 0)
        print(ress)
        return res

if __name__ == "__main__":
    s = "babgbag"
    t = "bag"
    S = Solution()
    print(S.numDistinct(s, t))
