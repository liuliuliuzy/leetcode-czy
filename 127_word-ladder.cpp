#include "basicInclude.h"

//下面这个超时了...
class Solution {
public:
    bool ifDifferOne(string s1, string refer){
        if(s1.size() != refer.size()) return false;
        int differCount = 0;
        for(int i=0; i<s1.size(); i++){
            if(s1[i] != refer[i]){
                differCount++;
            }
            if(differCount > 1){
                return false;
            }
        }
        return differCount == 1;
    }
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        //如果结尾单词不在wordList中
        if(find(wordList.begin(), wordList.end(), endWord) == wordList.end()) return 0;
        queue<string> s1, s2;
        vector<bool> flags(wordList.size(), false);
        s1.push(beginWord);
        int ans = 0;
        while (!s1.empty() || !s2.empty())
        {
            ans++;
            if(s2.empty()){
                while(!s1.empty()){
                    string tmpStr = s1.front();
                    s1.pop();
                    for(int i=0; i<wordList.size(); i++){
                        if(ifDifferOne(tmpStr, wordList[i]) && !flags[i]){
                            if(wordList[i] == endWord){
                                return ans+1;
                            }
                            else {
                                flags[i] = true;
                                s2.push(wordList[i]);
                            }
                        }
                    }
                }
            }
            else {
                while(!s2.empty()){
                    string tmpStr = s2.front();
                    s2.pop();
                    for(int i=0; i<wordList.size(); i++){
                        if(ifDifferOne(tmpStr, wordList[i]) && !flags[i]){
                            if(wordList[i] == endWord){
                                return ans+1;
                            }
                            else {
                                flags[i] = true;
                                s1.push(wordList[i]);
                            }
                        }
                    }
                }
            }
        }
        return 0;
    }
};

class otherSolution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {

        unordered_set<string> dict(wordList.begin(), wordList.end());
        if (dict.find(endWord) == dict.end() ) return 0;
        // 初始化起始和终点
        unordered_set<string> beginSet, endSet, tmp, visited;
        beginSet.insert(beginWord);
        endSet.insert(endWord);
        int len = 1;

        while (!beginSet.empty() && !endSet.empty()){
            if (beginSet.size() > endSet.size()){
                tmp = beginSet;
                beginSet = endSet;
                endSet = tmp;
            }
            tmp.clear();
            for ( string word : beginSet){
                for (int i = 0; i < word.size(); i++){
                    char old = word[i];
                    for ( char c = 'a'; c <= 'z'; c++){
                        if ( old == c) continue;
                        word[i] = c;
                        if (endSet.find(word) != endSet.end()){
                            return len+1;
                        }
                        if (visited.find(word) == visited.end() && dict.find(word) != dict.end()){
                            tmp.insert(word);
                            visited.insert(word);
                        }
                    }
                    word[i] = old;
                }
            }
            beginSet = tmp;
            len++;
            

        }
        return 0;
    }
};

int main()
{
    string s1 = "hit";
    string s2 = "cog";
    vector<string> wordList = {"hot","dot","dog","lot","log","cog"};
    otherSolution s;
    cout<<s.ladderLength(s1, s2, wordList)<<endl;
    return 0;
}