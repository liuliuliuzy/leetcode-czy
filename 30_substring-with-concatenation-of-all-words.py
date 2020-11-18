from typing import List
import collections

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dt = collections.defaultdict(list)
        dt2 = collections.defaultdict(str)
        used = []
        res = []
        for word in words:
            if word not in used:
                used.append(word)
            else:
                continue
            # tmp = []
            start = 0
            index = s.find(word, start)
            while index != -1:
                # tmp.append(index)
                # if index not in dt[word]:
                dt[word].append(index)
                start = index+1
                index = s.find(word, start)
        
        for word in used:
            for startIndex in dt[word]:

        return res

if __name__ == "__main__":
    S = Solution()
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    S.findSubstring(s, words)