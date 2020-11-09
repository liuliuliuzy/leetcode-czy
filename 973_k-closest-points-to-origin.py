from typing import List
import collections


class Solution:
    def __init__(self, name: str):
        self.name = name

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        堆排序

        如果是输出前k个最近的节点，那么是降序堆排列，构造小顶堆即可
        '''
        n_len = len(points)

        def calcu_dis(point: List[int]) -> int:
            return point[0] * point[0] + point[1] * point[1]

        def heap_adjust(start: int, end: int):
            dad = start
            son = dad * 2 + 1
            while son <= end:
                if son + 1 <= end and calcu_dis(points[son+1]) < calcu_dis(points[son]):
                    son += 1
                # print(dad, son)
                if calcu_dis(points[dad]) < calcu_dis(points[son]):
                    break
                else:
                    points[dad], points[son] = points[son], points[dad]
                    dad = son
                    son = dad * 2 + 1
        
        for i in range(n_len//2 - 1, -1, -1):
            heap_adjust(i, n_len-1)

        # print(points)
        j = n_len - 1
        # res = []
        for _ in range(K):
            points[j], points[0] = points[0], points[j]
            heap_adjust(0, j - 1)
            j -= 1

        return points[-1 * K:]
    
    def heap_Sort(self, numbers: List[int]) -> List[int]:
        n_len = len(numbers)
        def heap_adjust(start: int, end: int):
            '''
            start: 起始节点
            end: 节点的比较范围边界
            这个函数就做一件事，从开始节点出发，不断地调整其子树，使得符合大顶堆、小顶堆的顺序
            '''
            dad = start
            son = dad * 2 + 1
            while son <= end:
                if son + 1 <= end and numbers[son+1] > numbers[son]:
                    son += 1
                if numbers[dad] > numbers[son]:
                    break
                else:
                    numbers[dad], numbers[son] = numbers[son], numbers[dad]
                    dad = son
                    son = dad*2+1
        
        # 构造大顶堆
        for i in range(n_len//2-1, -1, -1):
            heap_adjust(i, n_len-1)
        
        # 替换元素并不断维持大顶堆性质
        for j in range(n_len-1, 0, -1):
            numbers[j], numbers[0] = numbers[0], numbers[j]
            heap_adjust(0, j-1)
        
        return numbers



if __name__ == "__main__":
    s = Solution('test')
    numbers = [2, 1, 4, 3, 7]
    points = [[5,-1],[3,3],[-2,4]]
    k = 2
    print(s.kClosest(points, k))
            
