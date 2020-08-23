#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

// class Solution {
// public:
//     vector<int> getRest(vector<int>& nums, int i, int j, char op){
//         vector<int> res;
//         for(int k=0; k<nums.size(); k++){
//             if(k!=i && k!=j){
//                 res.push_back(nums[k]);
//             }
//         }
//         switch (op)
//         {
//         case '+':
//             res.push_back()
//             break;
//         case '-':
//             /* code */
//             break;
//         case '*':
//             /* code */
//             break;
//         case '/':
//             /* code */
//             break;
//         default:
//             break;
//         }
//         return res;
//     }
//     bool judgePoint24(vector<int>& nums) {
//         if(nums.size() == 1){
//             return abs(nums[0]-24)<1e-6;
//         }
//         for(int i=0; i<nums.size()-1; i++){
//             for(int j=i+1; j<nums.size(); j--){
//                 if(judgePoint24())
//             }
//         }
//         return true;
//     }
//     void test(){
//         vector<int> test = {2, 3, 1, 4, 6};
//         vector<int> as = getRest(test, 2, 0);
//         for(auto num: as){
//             printf("%d ", num);
//         }
//         printf("%s", "\n");
//     }
// };


//CV, 我疯狂地cv
class Solution {
public:
    static constexpr int TARGET = 24;
    static constexpr double EPSILON = 1e-6;
    static constexpr int ADD = 0, MULTIPLY = 1, SUBTRACT = 2, DIVIDE = 3;

    bool judgePoint24(vector<int> &nums) {
        vector<double> l;
        for (const int &num : nums) {
            l.emplace_back(static_cast<double>(num));
        }
        return solve(l);
    }

    bool solve(vector<double> &l) {
        if (l.size() == 0) {
            return false;
        }
        if (l.size() == 1) {
            return fabs(l[0] - TARGET) < EPSILON;
        }
        int size = l.size();
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i != j) {
                    vector<double> list2 = vector<double>();
                    for (int k = 0; k < size; k++) {
                        if (k != i && k != j) {
                            list2.emplace_back(l[k]);
                        }
                    }
                    for (int k = 0; k < 4; k++) {
                        if (k < 2 && i > j) {
                            continue;
                        }
                        if (k == ADD) {
                            list2.emplace_back(l[i] + l[j]);
                        } else if (k == MULTIPLY) {
                            list2.emplace_back(l[i] * l[j]);
                        } else if (k == SUBTRACT) {
                            list2.emplace_back(l[i] - l[j]);
                        } else if (k == DIVIDE) {
                            if (fabs(l[j]) < EPSILON) {
                                continue;
                            }
                            list2.emplace_back(l[i] / l[j]);
                        }
                        if (solve(list2)) {
                            return true;
                        }
                        list2.pop_back();
                    }
                }
            }
        }
        return false;
    }
};

int main()
{
    Solution s;
    vector<int> x = {4,1,8,7};
    // printf(s.judgePoint24(x)?"true":"false");
    s.test();
    return 0;
}