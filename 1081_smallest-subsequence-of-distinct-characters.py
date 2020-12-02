# from random import randrange
from zyRandom import createRandomStr
import collections
from random import seed

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        '''
        返回字典顺序最小且含有s中每个不同字符的子串
        示例：
        输入："cdadabcc"
        输出："adbc"

        思路错误
        gg
        '''
        dfCounts = []
        items = []
        for i in range(len(s)-1, -1, -1):
            if s[i] not in items:
                items.append(s[i])
            dfCounts.insert(0, len(items))
        # print(dfCounts, items)

        res = ""
        i = 0
        while i < len(s):
            # if dfCounts[i] > len(items) - len(res):
            #     while res and res[-1] > s[i] and dfCounts[i] > len(items) - len(res):
            #         res = res[:-1]
            #     if len(res) < len(items):
            #         res += s[i]
            # else:
            #     res += s[i:]
            #     break
            if i == 0 or (i > 1 and dfCounts[i] != dfCounts[i-1]):
                res += s[i]
            else:
                if s[i] < res[-1]:
                    res = res[-1] + s[i]
            i += 1            
        return res

    def smallestSubsequenceII(self, s: str) -> str:
        '''
        https://leetcode-cn.com/problems/create-maximum-number/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-7/
        '''
        seen = set()
        res = []
        dt = collections.Counter(s)
        for c in s:
            if c not in seen:
                while res and c < res[-1] and dt[res[-1]] > 0:
                    seen.discard(res.pop())
                seen.add(c)
                res.append(c)
            dt[c] -= 1         
        return "".join(res)



if __name__ == "__main__":
    S = Solution()
    string = createRandomStr(34, -1)
    # string = "cdadabcc"
    print(string)
    print(S.smallestSubsequenceII(string))
