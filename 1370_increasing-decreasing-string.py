import collections

class Solution:
    def sortStringBad(self, s: str) -> str:
        '''
        写乱了...弃😓
        '''
        sl = list(s)
        sl.sort()
        flags = [False for i in range(len(sl))]
        res = "" + sl[0]
        goAhead = True
        index = 1
        while len(res) < len(s):
            if goAhead:
                while flags[index] or (index <= len(sl) - 1 and sl[index] <= res[-1]):
                    index += 1
                if index > len(sl) - 1:
                    index = len(sl) - 1
                    goAhead = False
                    continue
                res += sl[index]
                flags[index] = True
            else:
                while flags[index] or (index >= 0 and sl[index] >= res[-1]):
                    index -= 1
                if index < 0:
                    index = 1
                    continue
                res += sl[index]
                flags[index] = True


        # for ch in s:
        return s
    
    def sortString(self, s: str) -> str:
        '''
        字典记录各个字母出现的次数
        '''
        counts = collections.Counter(s)
        maxCeil = counts.most_common()[0][1] # 最大出现次数
        counts = sorted(counts.items()) # 按照字母键排序，返回一个元组数组
        ceil = 1 # 当前层数
        initIndex = 0 # 初始索引
        initFlag = 1 # 是从小到大还是从大到小
        res = ""
        while ceil <= maxCeil:
            while initIndex >=0 and initIndex <= len(counts)-1:
                # 当前字母的总出现次数高于当前层数，才会将其加到结果字符串末尾
                if counts[initIndex][1] >= ceil:
                    res += counts[initIndex][0]
                initIndex += initFlag
            # 调转遍历方向
            if initIndex < 0:
                initIndex = 0
                initFlag = 1
            else:
                initIndex = len(counts) - 1
                initFlag = -1
            # 进入下一层遍历
            ceil += 1
        return res

if __name__ == "__main__":
    s = Solution()
    st = "woshiliuziyang"
    print(s.sortString(st))
