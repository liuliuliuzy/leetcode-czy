class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        '''
        动态规划
        
        使用一维数组降低空间复杂度
        '''
        n1 = len(ring)
        n2 = len(key)
        dp = [n1*n2 for i in range(n1)]
        pos = [[] for j in range(n2)]
        for i in range(n2):
            for j in range(n1):
                if ring[j] == key[i]:
                    pos[i].append(j)
        # pos[i]表示key[i]出现在ring中的位置集合
        # dp初始化
        for j in pos[0]:
            dp[j] = min(j, n1-j)+1

        # print(dp)
        # 开始动态规划
        for i in range(1, n2):
            tmpDp = [n1*n2 for i in range(n1)]
            for j in pos[i]:
                for k in pos[i-1]:
                    tmpDp[j] = min(tmpDp[j], dp[k]+min(abs(j-k), n1-abs(j-k))+1)
            dp = tmpDp[:]
            # print(dp)
        res = n1*n2
        for j in pos[n2-1]:
            res = min(res, dp[j])

        return res

    def findRotateStepsMul(self, ring: str, key: str) -> int:
        '''
        动态规划

        老老实实二维数组dp
        '''
        n1 = len(ring)
        n2 = len(key)
        dp = [[n1*n2 for i in range(n1)] for j in range(n2)]
        pos = [[] for j in range(n2)]
        for i in range(n2):
            for j in range(n1):
                if ring[j] == key[i]:
                    pos[i].append(j)
        # pos[i]表示key[i]出现在ring中的位置集合
        # dp初始化
        for j in pos[0]:
            dp[0][j] = min(j, n1-j)+1

        # 开始动态规划
        for i in range(1, n2):
            for j in pos[i]:
                for k in pos[i-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k]+min(abs(j-k), n1-abs(j-k))+1)
        res = n1*n2
        for j in pos[n2-1]:
            res = min(res, dp[n2-1][j])

        return res

if __name__ == "__main__":
    ring = 'godding'
    key = 'godding'
    s = Solution()
    print(s.findRotateSteps(ring, key))
    print(s.findRotateStepsMul(ring, key))