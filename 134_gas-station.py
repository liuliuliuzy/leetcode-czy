from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 0: return -1
        if len(gas) == 1 and gas[0] >=cost[0]: return 0

        def judge(i: int) -> bool:
            if i < 0 or i >= len(gas): return False
            start = i
            count = 0
            now = 0
            while count < len(gas):
                now += gas[start] - cost[start]
                if now < 0:
                    return False
                if start == len(gas) - 1:
                    # now -= cost[start] - gas[0]
                    start = 0
                else:
                    # now -= cost[start] - gas[start+1]
                    start += 1
                # if now < 0:
                #     return False
                count += 1
            return True

        for i in range(len(gas)):
            last = 0
            if i == 0:
                last = len(gas) - 1
            else:
                last = i - 1
            if gas[last] - cost[last] <= 0 and gas[i] - cost[i] > 0:
                if judge(i): return i
            else:
                continue
            # print(judge(i))
        return -1

if __name__ == "__main__":
    gas  = [2,3,4]
    cost = [3,4,3]
    s = Solution()
    print(s.canCompleteCircuit(gas, cost))