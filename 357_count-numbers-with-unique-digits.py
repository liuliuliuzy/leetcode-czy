class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        '''
        这题应该用数学方法来做
        '''
        # n大于10的话，因为超出10位的数字必然会有重复位，所以和n=10的情况相同
        if n > 10:
            return self.countNumbersWithUniqueDigits(10)
        if not n:
            return 1
        res, muls = 10, 9
        for i in range(1, n):
            muls *= 10 - i
            res += muls
        return res

    def countNumbersWithUniqueDigitsII(self, n: int) -> int:
        '''
        回溯算法来一遍
        '''
        # 记录0~9的使用情况
        if not n: return 1
        used = [0 for i in range(10)]
        # 目标
        def backtrack(n: int, start: int) -> int:
            if start == n:
                return 0
            count = 0
            for i in range(10):
                if (start == 1 and i == 0 and n > 1) or used[i]:
                    continue
                used[i] = 1
                count += backtrack(n, start+1) + 1
                used[i] = 0
            return count
        return backtrack(min(10, n), 0)


if __name__ == "__main__":
    s = Solution()
    for i in range(1, 11):
        print(s.countNumbersWithUniqueDigitsII(i))