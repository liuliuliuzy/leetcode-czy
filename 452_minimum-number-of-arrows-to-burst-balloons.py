from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        数组重叠区间问题
        最坏O(n^2)
        '''
        def getCommon(interVal1: List[int], interVal2: List[int]) -> List[int]:
            if interVal1[1] < interVal2[0] or interVal2[1] < interVal1[0]:
                return []
            else:
                return [max(interVal1[0], interVal2[0]), min(interVal1[1], interVal2[1])]

        if len(points) < 2: return len(points)
        points.sort(key=lambda x: x[0])
        commonIntervals = [points[0]]
        res = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i][1]:
                commonIntervals.append(points[i])
                res += 1
                continue
            tmpFlag = False
            for j in range(len(commonIntervals)):
                tmp = getCommon(points[i], commonIntervals[j])
                if tmp:
                    # 更新区间
                    commonIntervals[j] = tmp
                    tmpFlag = True
                    break
            if not tmpFlag:
                # 添加新的区间
                commonIntervals.append(points[i])
                res += 1
            # print(commonIntervals)
        
        return res

    def findMinArrowShotsII(self, points: List[List[int]]) -> int:
        if len(points) < 2: return len(points)
        points.sort(key = lambda item: item[0])
        res = 1
        interVal = points[0]
        start = 1
        while start < len(points):
            if points[start][0] <= interVal[1]:
                interVal = [points[start][0], min(points[start][1], interVal[1])]
            else:
                res += 1
                interVal = points[start]
            start += 1
        return res


if __name__ == "__main__":
    s = Solution()
    points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
    # points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    print(s.findMinArrowShotsII(points))
        