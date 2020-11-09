from typing import List

class Solution:
    '''
    维护两个量：当前买入价格与当前最大利润
    从第一个价格出发往后遍历，碰到小的就替换为当前的买入价格，碰到比当前买入价格高的，就计算卖出所得利润，如果高于当前的利润，就将其更新为更大值
    这种方法的有效性：
    每次计算利润的时候，能够确保这是以该价格卖出而能够得到的最大利润，因为在之前的便利中，我们总是取最小的买入价格
    而不断地对比更新利润值，则保证了最终结果的正确性
    '''
    # 只有一次交易机会
    def maxProfit(self, prices: List[int]) -> int:
        buyIn = prices[0]
        profit = 0
        sell = -1
        for i in range(1, len(prices)):
            if prices[i] > buyIn:
                if prices[i] - buyIn > profit:
                    profit = prices[i] - buyIn
            else:
                buyIn = prices[i]
        
        return profit

    # 有多次交易机会
    def maxProfitII(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buyIn = prices[0]
        index = 1
        totalProfit = 0
        while index < len(prices):
            if buyIn < 0:
                buyIn = prices[index]
                index += 1
                continue
            if prices[index] < buyIn:
                buyIn = prices[index]
            else:
                while index < len(prices)-1 and prices[index+1] > prices[index]:
                    index += 1
                totalProfit += (prices[index] - buyIn)
                buyIn = -1
            index += 1
        return totalProfit

    # 买卖股票II的简化版解法，这么简单，有种作弊的感觉
    def maxProfitII_simple(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1, 0, -1):
            if prices[i] > prices[i-1]:
                res += (prices[i]-prices[i-1])
        return res

    # 只有两次交易机会，动态规划
    def maxProfitIII(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # dp 数组，dp[k][j][i] 表示第k+1天的时候，持有股票状态为j（j=0未持有，j=1持有），已经完成的交易次数为i次的时候，所能够获取的利润的最大值
        dp = [ [ [0 for i in range(3)] for j in range(2)] for k in range(n)]
        dp[0][1][0] = dp[0][1][1] = dp[0][1][2] = -prices[0]
        dp[0][0][0] = dp[0][0][1] = dp[0][0][2] = 0

        for k in range(1, len(prices)):
            dp[k][0][0] = 0
            dp[k][0][1] = max(dp[k-1][0][1], dp[k-1][1][0]+prices[k])
            dp[k][0][2] = max(dp[k-1][0][2], dp[k-1][1][1]+prices[k])

            dp[k][1][0] = max(dp[k-1][1][0], dp[k-1][0][0]-prices[k])
            dp[k][1][1] = max(dp[k-1][1][1], dp[k-1][0][1]-prices[k])
            dp[k][1][2] = 0
        return max(dp[len(prices)-1][0][1], dp[len(prices)-1][0][2])

    # 最多可以完成K笔交易，同样也是动态规划           
    def maxProfitIV(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        if k >= n//2:
            buyIn = prices[0]
            total = 0
            for i in range(1, n):
                if prices[i]<buyIn:
                    buyIn = prices[i]
                else:
                    total += prices[i]-buyIn
                    buyIn = prices[i]
            return total
        
        dp = [ [ [0 for i in range(k+1)] for j in range(2)] for m in range(n)]
        
        for j in range(k+1):
            dp[0][0][j] = 0
            dp[0][1][j] = -prices[0]
        for i in range(1, n):
            for j in range(k+1):
                if j == 0:
                    # dp[i][0][j] = 0
                    dp[i][1][j] = max(dp[i-1][1][j], dp[i-1][0][0]-prices[i])
                    continue
                if j == k:
                    dp[i][0][j] = max(dp[i-1][0][j], dp[i-1][1][j-1]+prices[i])
                    dp[i][1][j] = 0
                    continue
                dp[i][0][j] = max(dp[i-1][0][j], dp[i-1][1][j-1]+prices[i])
                dp[i][1][j] = max(dp[i-1][1][j], dp[i-1][0][j]-prices[i])

        return dp[n-1][0][k]

if __name__ == "__main__":
    prices = [3,2,6,5,0,3]
    s = Solution()
    print(s.maxProfitIV(2, prices))
