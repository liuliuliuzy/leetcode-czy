from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


if __name__ == "__main__":
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    s = Solution()
    print(s.arrayStringsAreEqual(word1, word2))