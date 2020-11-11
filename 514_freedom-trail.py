class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        '''
        动态规划
        '''
        n1 = len(ring)
        n2 = len(key)
        dp = []
        initStep = initIndexOfRing = 0
        for i in range(n2):
        
        return 1

if __name__ == "__main__":
    ring = 'godding'
    key = 'gd'
    s = Solution()
    print(s.findRotateSteps(ring, key))