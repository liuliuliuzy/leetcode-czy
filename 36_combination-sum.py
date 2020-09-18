from typing import List
#回溯算法，练手
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        tmp = []
        def recu(index, res):
            #终止条件
            if index >= len(candidates) or res >= target:
                if res == target:
                    #注意这里的列表深拷贝
                    ans.append(tmp[:])
                return
            tmp.append(candidates[index])
            recu(index, res+candidates[index])
            tmp.pop()
            recu(index+1, res)
        recu(0, 0)
        return ans

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    s = Solution()
    print(s.combinationSum(candidates, target))