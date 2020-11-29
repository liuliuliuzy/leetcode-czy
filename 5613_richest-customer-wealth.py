from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        accounts.sort(key=lambda x: sum(x))
        return sum(accounts[-1])

if __name__ == "__main__":
    s = Solution()
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    print(s.maximumWealth(accounts))