from typing import List

class Solution:
    '''
    leetcode 93, 往字符串中插入 '.' 分隔符，来复原可用的IP地址
    '''
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        有很多可以优化剪枝的地方诶
        '''
        # 存储所有合法的结果
        res = []
        total = []
        path = []
        n = len(s)
        if n > 12:
            return res

        def backtrack(path: List[int], start: int, length: int):
            if length == 3:
                if judge(path):
                    res.append(path[:])
            for i in range(start, min(start+4, n-1)):
                path.append(i)
                backtrack(path, i+1, length+1)
                path.pop()
            
        def judge(path):
            if path in res:
                return False
            if len(path) != 3:
                return False
            a1 = s[:path[0]+1]
            a2 = s[path[0]+1:path[1]+1]
            a3 = s[path[1]+1:path[2]+1]
            a4 = s[path[2]+1:]
            if judgeOne(a1) and judgeOne(a2) and judgeOne(a3) and judgeOne(a4):
                total.append('.'.join([a1, a2, a3, a4]))
                return True

        def judgeOne(s: str) -> bool:
            if len(s) > 3 or (len(s) > 1 and s[0] == '0') or int(s) > 255:
                return False
            return True

        backtrack(path, 0, 0)
        return total


def judgeOne(s: str) -> bool:
    if len(s) > 3 or (len(s) > 1 and s[0] == '0') or int(s) > 255:
        return False
    return True


if __name__ == "__main__":
    s = Solution()
    text = "010010"
    print(s.restoreIpAddresses(text))
        
