from typing import List

class Solution:
    # 超时了，窝淦
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
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
    
    

if __name__ == "__main__":
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    solu = Solution()
    print(solu.wordBreak(s, wordDict))

                    
                    