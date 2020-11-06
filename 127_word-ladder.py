from typing import List
import collections

# BFS-Breadth first Search
class Solution:
    # 构造有向图
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        
        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                # 加入虚拟节点
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        # 记录节点与节点ID对应信息
        wordId = dict()
        # 记录边信息，邻接表
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)
        addEdge(beginWord)

        if endWord not in wordId:
            return 0
        
        # 初始距离记录
        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        # 起点节点的距离为0
        dis[beginId] = 0

        # 从一个节点开始，广度优先搜索，并且维护距离数组dis
        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            # 如果到达了自己想要查找的节点
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                # 如果没有遍历过
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)     
        return 0

# 双向广度优先，优化，提高执行速度
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        
        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        # 构造图的过程方式一样的，空间复杂度相同 maybe
        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)
        
        addEdge(beginWord)
        if endWord not in wordId:
            return 0
        
        disBegin = [float("inf")] * nodeNum
        beginId = wordId[beginWord]
        disBegin[beginId] = 0
        queBegin = collections.deque([beginId])

        disEnd = [float("inf")] * nodeNum
        endId = wordId[endWord]
        disEnd[endId] = 0
        queEnd = collections.deque([endId])

        while queBegin or queEnd:
            queBeginSize = len(queBegin)
            for _ in range(queBeginSize):
                nodeBegin = queBegin.popleft()
                if disEnd[nodeBegin] != float("inf"):
                    return (disBegin[nodeBegin] + disEnd[nodeBegin]) // 2 + 1
                for it in edge[nodeBegin]:
                    if disBegin[it] == float("inf"):
                        disBegin[it] = disBegin[nodeBegin] + 1
                        queBegin.append(it)

            queEndSize = len(queEnd)
            for _ in range(queEndSize):
                nodeEnd = queEnd.popleft()
                if disBegin[nodeEnd] != float("inf"):
                    return (disBegin[nodeEnd] + disEnd[nodeEnd]) // 2 + 1
                for it in edge[nodeEnd]:
                    if disEnd[it] == float("inf"):
                        disEnd[it] = disEnd[nodeEnd] + 1
                        queEnd.append(it)
        
        return 0

class Test:
    def testFun(self):
        def test():
            nonlocal count
            print(count)
            count += 1
            # nonlocal dic
            dic.append(1)
            # print(count)

        dic = []
        count = 1
        test()
        print(dic)
        print(count)

if __name__ == "__main__":
    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(s.ladderLength(beginWord, endWord, wordList))
