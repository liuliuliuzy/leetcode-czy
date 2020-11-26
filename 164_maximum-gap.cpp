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
    int partition(vector<int> &nums, int start, int end){
        /*
        这么看来，选取数组中间的值作为pivot是最合适的，而且实现也比较简单易懂
        */
        int pivotIndex = start + (end - start) / 2;
        int pivotValue = nums[pivotIndex];
        int i = start, j = end;
        int temp;
        while(i <= j) {
            // 这里pivotValue是在初始的i的左边，所以不需要担心i的索引越界问题
            while(nums[i] < pivotValue) {
                i++;
            }
            while(nums[j] > pivotValue) {
                j--;
            }
            if(i <= j) {
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i++;
                j--;
            }
        }
        return i;
    }
    void quickSort(vector<int> &nums, int start, int end){
        if(start < end)
        {
            int j = partition(nums, start, end);
            quickSort(nums, start, j-1);
            quickSort(nums, j, end);
        } 
    }
    int maximumGapII(vector<int> &nums){
        if(nums.size() < 2) return 0;
        quickSort(nums, 0, nums.size()-1);
        int res = nums[1] - nums[0];
        for(int i=2; i<nums.size(); i++)
        {
            if(nums[i] - nums[i-1] > res)
            {
                res = nums[i] - nums[i-1];
            }
        }
        return res;
    }
};

int main()
{
    vector<int> testNums = {9,8,7,6,5,4,3,2,1};
    Solution s;
    cout<<s.maximumGapII(testNums)<<endl;
    // s.quickSort(testNums, 0, (int)testNums.size()-1);
    // for(auto item: testNums)
    // {
    //     cout<<item<<" ";
    // }
    // cout<<endl;
    return 0;
}