class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        zNum = (k - n) // 25
        oneDis = (k - n) % 25
        return "a" * (n - zNum - 1) + chr(97 + oneDis) + "z" * zNum
