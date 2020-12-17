from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        greedy
        '''
        n = len(prices)
        if n < 2:
             return 0
        ans = 0
        minimum = prices[0]
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i]-fee-minimum
                minimum = prices[i]-fee
        return ans

if __name__ == "__main__":
    S = Solution()
    fee = 2
    prices = [1, 3, 2, 8, 4, 9]
    print(S.maxProfit(prices, fee))