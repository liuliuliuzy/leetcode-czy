#include <string>
#include <cstring>
#include <vector>
#include <cstdio>
#include <iostream>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() < 2){
            return strs.size()?strs[0]:"";
        }
        int start = 0;
        string ans = "";
        while (true)
        {
            if(strs[0].size() == 0){
                return "";
            }
            char tmpChar = strs[0][start];
            for(int i=1; i<strs.size(); i++){
                //如果不相等或者超出了范围
                if(strs[i][start] != tmpChar || start>(strs[i].size()-1)){
                    return ans;
                }
            }
            ans.push_back(tmpChar);
            start++;
        }
    }
};

int main()
{
    Solution s;
    vector<string> test = {"flower","flow","flight"};
    cout<<s.longestCommonPrefix(test)<<endl;
    return 0;
}