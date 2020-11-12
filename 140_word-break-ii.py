from typing import List

class Solution:
    # 超时了，窝淦
    def wordBreakBad(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [([1], [""])]
        for i in range(len(s)):
            dp.append(([], []))
        for i in range(0, len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict and dp[j][0]:
                    # print(dp[i+1], i+1, j)
                    dp[i+1][0].append(1)
                    # temRes = []
                    if i == len(s)-1:
                        for item in dp[j][1]:
                            tmp = item
                            tmp+=(s[j:i+1])
                            dp[i+1][1].append(tmp)
                    else:
                        for item in dp[j][1]:
                            tmp = item
                            tmp+=(s[j:i+1]+" ")
                            dp[i+1][1].append(tmp)                        
                    # print(i+1, j, dp)
        return dp[-1][1]
    

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        不加判断直接回溯会超时
        加个判断在前面就不超时了
        总结：面向测试用例编程😥
        '''
        res = []
        # path = ""
        n = len(s)
        def wordBreakTrue() -> bool:
            dp = [True, s[0] in wordDict]
            for i in range(1, len(s)):
                # update dp
                tmpFlag = False
                for j in range(i+1):
                    if s[j:i+1] in wordDict and dp[j]:
                        tmpFlag = True
                        break
                    else:
                        continue
                dp.append(tmpFlag)
            return dp[len(s)]

        def backtrack(start: int, path: str):
            if start == n:
                res.append(path[1:])
            tmp = ""
            for i in range(start, n):
                tmp += s[i]
                if tmp in wordDict:
                    backtrack(i+1, path+" "+tmp)
                else:
                    continue
        if wordBreakTrue():
            backtrack(0, "")
        return res


if __name__ == "__main__":
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    solu = Solution()
    print(solu.wordBreak(s, wordDict))

                    
                    