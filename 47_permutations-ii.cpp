#include "basicInclude.h"

using namespace std;

//definition of solution class
//backtrack
class Solution {
public:
    void dfs(vector<int>& nums, vector<bool>& used, vector<int>& sol, vector<vector<int>>& res){
        if(sol.size() == nums.size()){
            res.push_back(sol);
            return ;
        }
        for(int i=0; i<nums.size(); i++){
            if(used[i] || (i>0 && !used[i-1] && nums[i] == nums[i-1])){
                continue;
            }
            sol.push_back(nums[i]);
            used[i] = true;
            dfs(nums, used, sol, res);
            sol.pop_back();
            used[i] = false;
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        //sort
        sort(nums.begin(), nums.end());
        vector<bool> used(nums.size(), false);
        vector<vector<int>> res;
        vector<int> sol;
        dfs(nums, used, sol, res);
        return res;
    }
};

int main()
{
    Solution s;
    vector<int> nums = {1, 1, 2, 3};
    for(auto item: s.permuteUnique(nums)){
        for(auto number: item){
            printf("%d ", number);
        }
        printf("%c", '\n');
    }
    return 0;
}