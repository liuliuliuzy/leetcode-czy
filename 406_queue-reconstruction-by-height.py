from typing import List
import functools as fc

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        '''
        首先将people数组排序，规定[hi, ki]排在[hj, kj]前面，如果(hi >= hj or ki <= kj)
        然后遍历排序后的数组，将元素插入到初始为空的结果数组中
        '''
        def myCmp(item1: List[int], item2: List[int]) -> int:
            if item1[0] > item2[0]:
                return -1
            elif item1[0] < item2[0]:
                return 1
            elif item1[1] > item2[1]:
                return 1
            elif item1[1] < item2[1]:
                return -1
            else:
                return 0
        # # sorted(key=mykey) 也可
        # def myKey(item: List[int]):
        #     return (-1*item[0],item[1])
        
        people = sorted(people, key=fc.cmp_to_key(myCmp))
        res = []
        for item in people:
            res.insert(item[1], item)
        return res

if __name__ == "__main__":
    s = Solution()
    peoples = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(s.reconstructQueue(peoples))

'''
这可能是做过的leetcode上的最简单的题了
没看任何评论任何题解，只看到了贪心算法的标签，前后做完不超过20分钟
'''