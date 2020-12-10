from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if len(bills) == 0:
            return True
        if bills[0] != 5:
            return False
        dt = {5: 0, 10: 0}
        # print(dt[5])
        for item in bills:
            if item == 5:
                dt[5] += 1
            elif item == 10:
                if dt[5] > 0:
                    dt[5] -= 1
                else:
                    return False
                dt[10] += 1
            else:
                if dt[10] > 0 and dt[5] > 0:
                    dt[10] -= 1
                    dt[5] -= 1
                else:
                    if dt[5] > 2:
                        dt[5] -= 3
                    else:
                        return False
        return True

if __name__ == "__main__":
    S = Solution()
    x = [5, 5, 5, 10, 20, 5,5, 20]
    print(S.lemonadeChange(x))