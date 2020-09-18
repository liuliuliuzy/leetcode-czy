#include "basicInclude.h"

class Solution {
public:
    void dfs(int beginIndex, int n, vector<int>& nums, vector<int>& tmp, vector<vector<int>>& res){
        // if(tmp.size()>0 && tmp.size()<nums.size()){
        res.emplace_back(tmp);
        // }
        for(int i=beginIndex; i<n; i++){
            tmp.push_back(nums[i]);
            dfs(i+1, n, nums, tmp, res);
            tmp.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> tmp;
        dfs(0, nums.size(), nums, tmp, res);
        return res;
    }
};

class newSolution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res = {{}};
        for (int i = nums.size()-1; i >=0; i--)
        {
            vector<vector<int>> tmpRes = res;
            for(auto item: tmpRes){
                item.insert(item.begin(), nums[i]);
                res.push_back(item);
            }
        }
        return res;
    }  
};

int main()
{
    newSolution s;
    vector<int> nums = {1,2,3};
    for(auto item: s.subsets(nums)){
        for(auto number: item){
            printf("%d, ", number);
        }
        printf("%c", '\n');
    }
    return 0;
}