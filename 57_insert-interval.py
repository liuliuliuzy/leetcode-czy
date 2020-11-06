from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        added = False
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        if intervals[0][0] > newInterval[0]:
            intervals.insert(0, newInterval)
            if intervals[0][1] < intervals[1][0]:
                return intervals
            added = True
        if intervals[-1][0] < newInterval[0]:
            intervals.append(newInterval)
            if intervals[-1][0] > intervals[-2][1]:
                return intervals
            added = True
        if not added:
            for i in range(len(intervals)):
                if intervals[i][0] >= newInterval[0]:
                    intervals.insert(i, newInterval)
                    addedIndex = i
                    break
        # 再合并，一次遍历，解决多种可能的重叠情况，nice
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            # print(res[-1][1], intervals[i][0])
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res


if __name__ == "__main__":
    test = [[1, 2], [5, 7], [9, 13]]
    newItem = [2, 15]
    s = Solution()
    print(s.insert(test, newItem))



            