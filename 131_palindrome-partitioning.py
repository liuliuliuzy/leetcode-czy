from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        method1: dynamic programming

        遍历s长度i，需要维护一个表示s[:i]的分割方法的List[List[str]]类型变量

        time defeat: 9%
        memory defeat: 25%
        '''
        res = []
        if not s:
            return res
        n = len(s)
        res.append([s[0]])
        for i in range(1, n):
            k = len(res)
            for j in range(k):
                tmp = s[i]
                for t in range(len(res[j])-1, -1, -1):
                    tmp = res[j][t] + tmp
                    if tmp[::-1] == tmp:
                        tmpres = res[j][:t]
                        tmpres.append(tmp)
                        if tmpres not in res:
                            res.append(tmpres)
            for m in range(k):
                res[m].append(s[i])
        return res
    
    def partitionII(self, s: str) -> List[List[str]]:
        '''
        method2: backtrack

        遍历每个字符，可以选择分或者不分，这样就产生了一棵决策树

        time defeat: 32%
        memory defeat: 15%
        '''
        res = []
        if not s:
            return res
        n = len(s)
        path = [s[0]]
        def backtrack(path: List[str], start: int):
            if start == n:
                if path[-1][::-1] != path[-1]:
                    return
                res.append(path[:])
                return
            # 对于每个字符，有两种选择partitionII
            # 但是为了保证回文子串的要求，需要进行剪枝
            path[-1] += s[start]
            backtrack(path, start+1)
            path[-1] = path[-1][:-1]

            if path[-1][::-1] != path[-1]:
                return
            path.append(s[start])
            backtrack(path, start+1)
            path.pop()
        
        backtrack(path, 1)
        return res

            

if __name__ == "__main__":
    s = "aaba"
    Solution = Solution()
    print(Solution.partitionII(s))
