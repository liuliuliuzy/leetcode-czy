import collections
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        '''
        首先肯定要统计各个字符出现的次数
        '''
        count = []
        counter = collections.Counter(S)
        res = ""
        # 构造字母出现次数列表
        for key, value in counter.items():
            count.append([key, value])

        count.sort(key = lambda x: x[1])
        print(count)
        initChar, initCount = count.pop()
        i = 0
        while i < len(count):
            if initCount >= count[i][1]:
                res += (count[i][0] + initChar) * count[i][1]
                initCount -= count[i][1]
                count[i][1] = 0
            else:
                if i < len(count) - 1:
                    res += (count[i][0] + initChar) * initCount
                    count[i][1] -= initCount
                    initChar, initCount = count.pop()
                    res += (count[i][0] + initChar) * count[i][1]
                    initCount -= count[i][1]
                    count[i][1] = 0
                else:
                    print(i, initChar, initCount)
                    return ""
            i += 1
        if initCount > 1:
            return ""
        return res + initChar * initCount

# 官方题解
class Solution2:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S
        
        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ""
        
        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        ans = list()

        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)
            ans.extend([letter1, letter2])
            counts[letter1] -= 1
            counts[letter2] -= 1
            if counts[letter1] > 0:
                heapq.heappush(queue, (-counts[letter1], letter1))
            if counts[letter2] > 0:
                heapq.heappush(queue, (-counts[letter2], letter2))
        
        if queue:
            ans.append(queue[0][1])
        
        return "".join(ans)

if __name__ == "__main__":
    s = Solution()
    S = "rehrtwfwvsdfeqe"
    # X = "bdcdwdfdedsdsdadadadadd"
    # print(collections.Counter(X))
    print(s.reorganizeString(S))
