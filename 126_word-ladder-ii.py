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

        def backtrack(path: List[str], pathCount: int, tmpWord: str):
            if pathCount == minDis:
                if path[-1] == endWord:
                    res.append(path[:])
            else:
                # result = False
                # tmpWord = path[-1]
                tmpWordId = wordId[tmpWord]
                for ne in edge[tmpWordId]:
                    if idToWord[ne] in visited:
                        continue
                    visited.add(idToWord[ne])
                    if '*' not in idToWord[ne]:
                        path.append(idToWord[ne])
                    backtrack(path, pathCount+1, idToWord[ne])
                    if '*' not in idToWord[ne]:
                        path.pop()
                    visited.remove(idToWord[ne])
                

        for word in wordList:
            addEdge(word)
        if beginWord not in wordList:
            addEdge(beginWord)

        res = []
        visited = []

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
        visited.add(beginWord)
        # print(path)
        backtrack(path, 0, beginWord)
        
        return res

class Solution2:
    def findLadders(self, beginWord, endWord, wordList):
        if not endWord in wordList:
            return []
        hash=collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hash[word[:i]+"*"+word[i+1:]].append(word)
        def edges(word):
            for i in range(len(word)):
                for newWord in hash[word[:i]+'*'+word[i+1:]]:
                    if not newWord in marked:
                        yield newWord
        def findPath(end):
            res=[]
            for curr in end:
                for parent in path[curr[0]]:
                    res.append([parent]+curr)
            return res
        marked=set()
        path=collections.defaultdict(set)
        begin=set([beginWord])
        end=set([endWord])
        forward=True
        while begin and end:
            if len(begin)>len(end):
                begin,end=end,begin
                forward=not forward
            temp=set()
            for word in begin:
                marked.add(word)
            for word in begin:
                for w in edges(word):
                    temp.add(w)
                    if forward:
                        path[w].add(word)
                    else:
                        path[word].add(w)
            begin=temp
            if begin&end:
                res=[[endWord]]
                while res[0][0]!=beginWord:
                    res=findPath(res)
                return res
        return []

if __name__ == "__main__":
    beginWord = "cet"
    endWord = "ism"
    wordList =  [
        "kid","tag","pup","ail","tun","woo","erg","luz","brr",
        "gay","sip","kay","per","val","mes","ohs","now","boa",
        "cet","pal","bar","die","war","hay","eco","pub","lob",
        "rue","fry","lit","rex","jan","cot","bid","ali","pay",
        "col","gum","ger","row","won","dan","rum","fad","tut",
        "sag","yip","sui","ark","has","zip","fez","own","ump",
        "dis","ads","max","jaw","out","btu","ana","gap","cry",
        "led","abe","box","ore","pig","fie","toy","fat","cal",
        "lie","noh","sew","ono","tam","flu","mgm","ply","awe",
        "pry","tit","tie","yet","too","tax","jim","san","pan",
        "map","ski","ova","wed","non","wac","nut","why","bye",
        "lye","oct","old","fin","feb","chi","sap","owl","log",
        "tod","dot","bow","fob","for","joe","ivy","fan","age",
        "fax","hip","jib","mel","hus","sob","ifs","tab","ara",
        "dab","jag","jar","arm","lot","tom","sax","tex","yum",
        "pei","wen","wry","ire","irk","far","mew","wit","doe",
        "gas","rte","ian","pot","ask","wag","hag","amy","nag",
        "ron","soy","gin","don","tug","fay","vic","boo","nam",
        "ave","buy","sop","but","orb","fen","paw","his","sub",
        "bob","yea","oft","inn","rod","yam","pew","web","hod",
        "hun","gyp","wei","wis","rob","gad","pie","mon","dog",
        "bib","rub","ere","dig","era","cat","fox","bee","mod",
        "day","apr","vie","nev","jam","pam","new","aye","ani",
        "and","ibm","yap","can","pyx","tar","kin","fog","hum",
        "pip","cup","dye","lyx","jog","nun","par","wan","fey",
        "bus","oak","bad","ats","set","qom","vat","eat","pus",
        "rev","axe","ion","six","ila","lao","mom","mas","pro",
        "few","opt","poe","art","ash","oar","cap","lop","may",
        "shy","rid","bat","sum","rim","fee","bmw","sky","maj",
        "hue","thy","ava","rap","den","fla","auk","cox","ibo",
        "hey","saw","vim","sec","ltd","you","its","tat","dew",
        "eva","tog","ram","let","see","zit","maw","nix","ate",
        "gig","rep","owe","ind","hog","eve","sam","zoo","any",
        "dow","cod","bed","vet","ham","sis","hex","via","fir",
        "nod","mao","aug","mum","hoe","bah","hal","keg","hew",
        "zed","tow","gog","ass","dem","who","bet","gos","son",
        "ear","spy","kit","boy","due","sen","oaf","mix","hep",
        "fur","ada","bin","nil","mia","ewe","hit","fix","sad",
        "rib","eye","hop","haw","wax","mid","tad","ken","wad",
        "rye","pap","bog","gut","ito","woe","our","ado","sin",
        "mad","ray","hon","roy","dip","hen","iva","lug","asp",
        "hui","yak","bay","poi","yep","bun","try","lad","elm",
        "nat","wyo","gym","dug","toe","dee","wig","sly","rip",
        "geo","cog","pas","zen","odd","nan","lay","pod","fit",
        "hem","joy","bum","rio","yon","dec","leg","put","sue",
        "dim","pet","yaw","nub","bit","bur","sid","sun","oil",
        "red","doc","moe","caw","eel","dix","cub","end","gem",
        "off","yew","hug","pop","tub","sgt","lid","pun","ton",
        "sol","din","yup","jab","pea","bug","gag","mil","jig",
        "hub","low","did","tin","get","gte","sox","lei","mig",
        "fig","lon","use","ban","flo","nov","jut","bag","mir",
        "sty","lap","two","ins","con","ant","net","tux","ode",
        "stu","mug","cad","nap","gun","fop","tot","sow","sal",
        "sic","ted","wot","del","imp","cob","way","ann","tan",
        "mci","job","wet","ism","err","him","all","pad","hah",
        "hie","aim","ike","jed","ego","mac","baa","min","com",
        "ill","was","cab","ago","ina","big","ilk","gal","tap",
        "duh","ola","ran","lab","top","gob","hot","ora","tia",
        "kip","han","met","hut","she","sac","fed","goo","tee",
        "ell","not","act","gil","rut","ala","ape","rig","cid",
        "god","duo","lin","aid","gel","awl","lag","elf","liz",
        "ref","aha","fib","oho","tho","her","nor","ace","adz",
        "fun","ned","coo","win","tao","coy","van","man","pit",
        "guy","foe","hid","mai","sup","jay","hob","mow","jot",
        "are","pol","arc","lax","aft","alb","len","air","pug",
        "pox","vow","got","meg","zoe","amp","ale","bud","gee",
        "pin","dun","pat","ten","mob"]

    s = Solution2()
    print(s.findLadders(beginWord, endWord, wordList))