#include "basicInclude.h"


//这是我以为的题目规则：
//在所有的数不是位数相同的情况下，一个数不会前面自动补0去进行and
//but...
//然后题目的意思好像是将每个数的所有位都进行and操作，int长度为32位，所以每个数要看成32个bit进行操作
class Solution {
public:
    int helpK(int k1, int k2, int digits){
        if(k1 < 0 || k2 < 0 || k1 >= (int)pow(2, digits) || k2 >= (int)pow(2, digits) || k1 > k2){
            return -1;
        }
        int boundary = (int)pow(2, digits-1);
        if(k1 < boundary && k2 >= boundary){
            return 0;
        }
        else if(k1 < boundary && k2 < boundary){
            return helpK(k1, k2, digits-1);
        }
        else{
            return boundary+helpK(k1-boundary, k2-boundary, digits-1);
        }
    }
    int rangeBitwiseAnd(int m, int n) {
        int a1 = (int)floor(log(m)/log(2));
        int a2 = (int)floor(log(n)/log(2));
        if(a1 != a2){
            return (int)pow(2, a2);
        }
        else {
            int k1 = m-(int)pow(2, a1);
            int k2 = n-(int)pow(2, a1);
            return ((int)pow(2, a1))+helpK(k1, k2, a1);
        }
    }
    //修正版
    int rangeBitwiseAndV2(int m, int n) {
        int i = 0;
        while(m != n){
            m >>= 1;
            n >>= 1;
            i += 1;
        }
        return m << i;
    }
};

int main()
{
    Solution s;
    cout<<s.rangeBitwiseAnd(123, 43141)<<endl;
    return 0;
}