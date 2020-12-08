from typing import List

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        for i in range(1, (len(S)-1)//2+1):
            if i > 1 and S[0] == '0':
                continue
            # print(i)
            for j in range(i+1, min(len(S)-i+1, ((len(S)-i)//2)+i+1)):
                # print(j)
                # print(i, j, "||", S[:i], S[i:j])
                if j - i > 1 and S[i] == '0':
                    continue
                res = [int(S[:i]), int(S[i:j])]
                nextIndex = j
                flag = True
                while nextIndex < len(S):
                    nextSum = int(res[-1]) + int(res[-2])
                    nextS = str(nextSum)
                    lastIndex = nextIndex
                    nextIndex += len(nextS)
                    if nextIndex > len(S) or S[lastIndex:nextIndex] != nextS or (nextIndex-lastIndex > 1 and S[lastIndex] == '0' or int(S[lastIndex:nextIndex]) > pow(2,31)):
                        flag = False
                        break
                    res.append(nextSum)
                if flag:
                    return res
        
        return []

    def splitIntoFibonacciII(self, S: str) -> List[int]:
        '''
        官方题解，确实剪枝的地方多了一些，执行时间也更少，但是函数调用使得内存空间消耗更多
        '''
        ans = list()

        def backtrack(index: int):
            if index == len(S):
                return len(ans) >= 3
            
            curr = 0
            for i in range(index, len(S)):
                if i > index and S[index] == "0":
                    break
                curr = curr * 10 + ord(S[i]) - ord("0")
                if curr > 2**31 - 1:
                    break
                
                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and curr > ans[-2] + ans[-1]:
                    break
        
            return False
        
        backtrack(0)
        return ans

if __name__ == "__main__":
    S = Solution()
    # s = "0111122"
    s = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    print(S.splitIntoFibonacci(s))