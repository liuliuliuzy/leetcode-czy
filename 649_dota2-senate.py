from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # double stack
        Rs = deque()
        Ds = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                Rs.append(i)
            else:
                Ds.append(i)
        startTime = 0
        while Rs and Ds:
            if Rs[0] < Ds[0]:
                Ds.popleft()
                Rs.append(Rs.popleft()+len(senate))
            else:
                Rs.popleft()
                Ds.append(Ds.popleft()+len(senate))  
        if Rs:
            return 'Radiant'
        else:
            return 'Dire'
        

if __name__ == "__main__":
    S = Solution()
    se = "RRRRRRRRRDDDDDDDDDDDDDD"
    print(S.predictPartyVictory(se))