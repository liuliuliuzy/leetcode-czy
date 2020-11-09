from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        '''
        回溯算法
        '''
        visited = [0]
        total = int(pow(2, n))

        # 对于result变量的创建和赋值很关键，它影响了之后的执行流
        def backtrack(num: int, count: int):
            # 如果满足结束条件
            if count == total:
                return True
            result = False
            for i in range(n):
                tmp = 0
                if (num >> i) & 1:
                    tmp = num - pow(2, i)
                else:
                    tmp = num + pow(2, i)
                if tmp in visited:
                    continue
                visited.append(tmp)
                if backtrack(tmp, count+1):
                    result = True
                    break
                visited.pop()
            return result

        backtrack(0, 1)
        return visited
            
if __name__ == "__main__":
    s = Solution()
    print(s.grayCode(4))