#include "basicInclude.h"

class Solution {
public:
    int maximumGap(vector<int>& nums) {
        /*
        遍历数组并且维护四个变量：

        */
        if(nums.size() < 2) return 0;
        int left = nums[0], right = nums[1];
        int maxLeft = nums[0], maxRight = nums[1];
        for(int i=0; i<nums.size(); i++){
            if(nums[i] < left){
                if(left - nums[i] > maxRight - maxLeft){
                    maxLeft = nums[i];
                    maxRight = left;
                }
                left = nums[i];
            }
            else if(nums[i] > right){
                if(nums[i] - right > maxRight - maxLeft){
                    maxLeft = right;
                    maxRight = nums[i];
                }
                right = nums[i];
            }
            else{// 如果落在最大距离区间内
                
            }
        }
    }
    void quickSort(vector<int> &nums, int start, int end){
        int sentinel = nums[start];
        int i = start+1, j = end;
        while (i < j)
        {
            while (i < j && nums[i] <= sentinel)
            {
                i++;
            }
            while (j > i && nums[j] >= sentinel)
            {
                j--;
            }
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            
        }
        int tmp = nums[j];
        nums[j] = nums[start];
        nums[start] = tmp;
        quickSort(nums, start, j-1);
        quickSort(nums, j+1, end);
        
    }
    int maximumGapII(vector<int> &nums){
        return 0;
    }
};

int main()
{
    vector<int> testNums = {2,3,5,1,8};
    Solution s;
    // cout<<s.maximumGap(testNums)<<endl;
    s.quickSort(testNums, 0, (int)testNums.size());
    for(auto item: testNums)
    {
        cout<<item<<" ";
    }
    cout<<endl;
    return 0;
}