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
