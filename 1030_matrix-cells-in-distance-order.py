from typing import List
import collections

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def myKey(dot: List[int]) -> int:
            return abs(dot[0] - r0) + abs(dot[1] - c0)

        # 直接调用sort内置方法
        # res = [[i, j] for i in range(R) for j in range(C)]
        # res.sort(key=myKey)
        # return res

        # 插入排序——超时~
        # res = []
        # for i in range(R):
        #     for j in range(C):
        #         index = 0
        #         tmp = [i, j]
        #         for k in range(len(res)):
        #             if myKey(res[k]) < myKey(tmp):
        #                 index += 1
        #         res.insert(index, tmp)
        # return res

        # 数学方法——曼哈顿距离dis(A, B) = abs(xa - xb) + abs(ya - yb)
        # dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        # # 首先计算四个顶点到(r0, c0)的曼哈顿距离的最大值
        # maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        # row, col = r0, c0
        # ret = [[row, col]]
        # for dist in range(1, maxDist + 1):
        #     row -= 1
        #     for i, (dr, dc) in enumerate(dirs):
        #         while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
        #             if 0 <= row < R and 0 <= col < C:
        #                 ret.append([row, col])
        #             row += dr
        #             col += dc
        # return ret

        # 桶排序
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        bucket = collections.defaultdict(list)
        dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)

        for i in range(R):
            for j in range(C):
                bucket[dist(i, j, r0, c0)].append([i, j])

        ret = list()
        for i in range(maxDist + 1):
            ret.extend(bucket[i])
        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.allCellsDistOrder(3, 4, 1, 2))
