class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()    
        seen = []
        dt = {}
        i = 0
        if len(pattern) != len(words):
            return False
        for chara in pattern:
            if chara not in dt:
                if words[i] in seen:
                    return False
                dt[chara] = words[i]
                seen.append(words[i])
            else:
                if words[i] != dt[chara]:
                    return False
            i += 1
        return True

if __name__ == "__main__":
    S = Solution()
    pattern ='abba'
    words = 'dog dog dog dog'
    print(S.wordPattern(pattern, words))