from typing import List

# hint: dynamic prigramming
class Solution:
    # 递归会超时=.=
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        print("Got {}".format(s))
        for item in wordDict:
            if s == item:
                return True
            if s.startswith(item):
                print("Got item {}".format(item))
                if self.wordBreak(s[len(item):], wordDict):
                    return True
                else:
                    continue
        return False
    
    # 动态规划，思维
    def wordBreakTrue(self, s: str, wordDict: List[str]) -> bool:
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

        

class SolutionExample:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True, s[0] in wordDict]
        for i in range(1, len(s)):
            for j in range(i+1):
                if s[j: i+1] in wordDict and dp[j]:
                    dp.append(True)
                    break
            else:
                dp.append(False)
        return dp[-1]

if __name__ == "__main__":
    s = 'catsanddog'
    words = ['cat', 'cats', 'and', 'sand', 'dog']
    test = Solution()
    print(test.wordBreakTrue(s, wordDict=words))