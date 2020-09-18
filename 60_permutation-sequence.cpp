#include "basicInclude.h"

class Solution {
public:
    //recursive
    string helper(vector<int>& nums, int k){
        if(nums.size() == 1){
            return to_string(nums[0]);
        }
        int base = 1;
        for(int i=nums.size()-1; i>1; i--){
            base*=i;
        }
        int index = k/base;
        int newK = k%base;
        if(newK == 0){
            index-=1; 
            newK=base;
        }
        string tmp = to_string(nums[index]);
        // printf("%d %d\n", index, newK);
        nums.erase(nums.begin()+index);
        return tmp+helper(nums, newK);
    }
    string getPermutation(int n, int k) {
        vector<int> nums;
        for(int i=1; i<n+1; i++){
            nums.push_back(i);
        }
        return helper(nums, k);
    }
};

int main()
{
    Solution s;
    printf("%s\n", s.getPermutation(6, 7).c_str());
    return 0;
}