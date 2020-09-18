#include "basicInclude.h"

class Solution {
public:
    //ordinary method
    void dfs(vector<vector<int>>& res, vector<int>& tmp, int n, int k, int begin){
        if(k == 0){
            res.push_back(tmp);
            return ;
        }
        int nowSize = tmp.size();
        for(int i=begin; i<n-k+2; i++){
            // printf("%d, ", i);
            tmp.push_back(i);
            dfs(res, tmp, n, k-1, i+1);
            tmp.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(res, tmp, n, k, 1);
        return res;
    }
};

class newSolution {
public:
    //ordinary method
    void dfs(vector<vector<int>>& res, vector<int>& tmp, int n, int k, int begin){
        if(tmp.size() == k){
            res.push_back(tmp);
            return ;
        }
        int nowSize = tmp.size();
        for(int i=begin; i<n+1; i++){
            // printf("%d, ", i);
            tmp.push_back(i);
            dfs(res, tmp, n, k, i+1);
            tmp.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(res, tmp, n, k, 1);
        return res;
    }
};

int main()
{
    newSolution s;
    for(auto item: s.combine(6, 4)){
        for(auto number: item){
            printf("%d, ", number);
        }
        printf("%c", '\n');
    }
    return 0;
}