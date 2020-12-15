class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        '''
        从后往前，从简单到复杂
        '''
        ans = []
        digits = []
        while N > 0:
            digits.insert(0, N % 10)
            N = N // 10
        i = 0
        while i < len(digits) and (i == len(digits)-1 or digits[i] <= digits[i+1]):
            # ans = ans*10 + digits[i]
            ans.append(digits[i])
            i += 1
        if i < len(digits) - 1:
            tmp = digits[i]
            while ans and ans[-1] == tmp:
                ans.pop()
                i -= 1
            ans.append(digits[i] - 1)
            i += 1
            while i < len(digits):
                ans.append(9)
                i += 1
        res = 0
        for item in ans:
            res = res * 10 + item
        return res


if __name__ == "__main__":
    S = Solution()
    print(S.monotoneIncreasingDigits(1))