from typing import List
import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        '''
        思路仍然是回溯算法
        '''

        wordId = dict()
        idToWord = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0
        # 首先，BFS，构建无向图并且计算起点到目的节点的最短路径长度
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                idToWord[nodeNum] = word
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

        def backtrack(path: List[str], pathCount: int):
            if pathCount == minDis:
                if path[-1] == endWord:
                    res.append(path)
                return
            
            # result = False
            tmpWord = path[-1]
            tmpWordId = wordId[tmpWord]
            for ne in edge[tmpWordId]:
                path.append(idToWord[ne])
                backtrack(path, pathCount+1)
                path.pop()
                

        for word in wordList:
            addEdge(word)
        addEdge(beginWord)

        res = []

        if endWord not in wordList:
            return res

        # 初始距离记录
        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        # 起点节点的距离为0
        dis[beginId] = 0

        que = collections.deque()
        que.append(beginId)

        flag = False
        # 开始BFS
        while que:
            x = que.popleft()
            # 如果到达了自己想要查找的节点
            if x == endId:
                flag = True
                break
            for it in edge[x]:
                # 如果没有遍历过
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)

        if not flag:
            return res

        # 回溯
        visited = set()        
        minDis = dis[endId]
        path = [beginWord]
        print(path)
        backtrack(path, 1)

        return res


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    s = Solution()
    print(s.findLadders(beginWord, endWord, wordList))