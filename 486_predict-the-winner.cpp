#include "basicInclude.h"

//dp
class Solution {
public:
    // int maxScores(vector<int>& nums, bool isFirst){
    //     if(nums.size() == 1){
    //         return isFirst?nums[0]:0;
    //     }
    //     if(isFirst){
    //         return max(nums[0]+maxScores(nums[]))
    //     }
    // }
    bool PredictTheWinner(vector<int>& nums) {

    }
};

//玩家1先取，玩家2后取，计算两者的最大分数
int main()
{
    vector<int> nums = {1, 2, 3, 4, 5};
    Solution s;
    cout<<s.PredictTheWinner(nums)<<endl;
    return 0;
}