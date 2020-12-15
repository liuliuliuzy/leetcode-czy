from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        hash table
        '''
        dt = collections.defaultdict(list)
        for st in strs:
            tmpS = ''.join(sorted(st))
            # if st not in dt[tmpS]:
            dt[tmpS].append(st)

        return list(dt.values())
    
    def groupAnagramsII(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())
    
    def groupAnagramsIII(self, strs: List[str]) -> List[List[str]]:
        maps = {
            'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,
            'n':43,'o':47,'p':53,'q':59,'r':61,'s':67,'t':71,'u':73,'v':79,'w':83,'x':89,'y':97,'z':101
        }
        dt = {}
        for st in strs:
            res = 1
            for ch in st:
                res *= maps[ch]
            if res not in dt:
                dt[res] = []
            dt[res].append(st)
        return list(dt.values())

if __name__ == "__main__":
    S = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = ["abc", "abc"]
    print(S.groupAnagramsIII(strs))