#include "basicInclude.h"

class Solution {
public:
    bool isValid(vector<string>& sol, int i, int n){
        int index = sol.size();
        for(auto item: sol){
            if(item[i] == 'Q' || (i+index<n && item[i+index] == 'Q') || (i-index>=0 && item[i-index]=='Q')){
                return false;
            }
            index--;
        }
        return true;
    }
    void dfs(vector<vector<string>>& res, vector<string> sol, int n){
        if(sol.size() == n){
            res.push_back(sol);
            return ;
        }
        for(int i=0; i<n; i++){
            if(!isValid(sol, i, n)){
                continue;
            }
            string tmp(n, '.');
            tmp[i] = 'Q';
            sol.push_back(tmp);
            dfs(res, sol, n);
            sol.pop_back();
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> sol;
        dfs(res, sol, n);
        return res;
    }
};

int main()
{
    int x = 4;
    Solution s;
    for(auto item: s.solveNQueens(x)){
        for(auto str: item){
            printf("%s, ", str.c_str());
        }
        printf("%c", '\n');
    }
    return 0;
}