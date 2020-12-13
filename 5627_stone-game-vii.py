from typing import List

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        sA, sB = 0, 0
        if len(stones) == 2:
            return max(stones)
        while len(stones) > 0:
            # first Alice
            # if len(stones) > 2:
            #     if stones[-1] - max(stones[-1] - stones[1], 0) > stones[0] - max(stones[0] - stones[-2], 0):
            #         sA += sum(stones[1:])
            #         stones = stones[1:]
            #     else:
            #         sA += sum(stones[:-1])
            #         stones = stones[:-1]
            if len(stones) > 2:
                if stones[-1] > stones[0]:
                    sA += sum(stones[1:])
                    stones = stones[1:]
                else:
                    sA += sum(stones[:-1])
                    stones = stones[:-1]
            else:
                sA += max(stones)
                break


            # then bob
            if len(stones) > 2:
                if len(stones) > 2:
                    if stones[-1] - max(stones[-1] - stones[1], 0) <= stones[0] - max(stones[0] - stones[-2], 0):
                        sB += sum(stones[1:])
                        stones = stones[1:]
                    else:
                        sB += sum(stones[:-1])
                        stones = stones[:-1]
            else:
                sB += max(stones)
                break            
            print(sA, sB, stones)
        return sA -sB


    def stoneGameVII_new(self, stones: List[int]) -> int:
        '''
        dp
        '''

if __name__ == "__main__":
    S = Solution()
    # stones = [7,90,5,1,100,10,10,2]
    stones = [1,1,1,1,7,1,1,1,1,1,1,1,1,1,1]
    print(S.stoneGameVII(stones))