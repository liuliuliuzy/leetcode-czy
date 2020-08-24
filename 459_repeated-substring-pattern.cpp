#include "basicInclude.h"

class Solution {
public:
    //很不幸，下面这个超时了...可能是判断字符串相等这里太耗时间了
    // bool repeatedSubstringPattern(string s) {
    //     for(int l=1; l<(int)floor(s.size()/2)+1; l++){
    //         string subStr = s.substr(0, l);
    //         if( (s+subStr) == (subStr+s) ){
    //             return true;
    //         }
    //     }
    //     return false;
    // }
    //正确的解法见同题号py文件
    bool repeatedSubstringPattern(string s) {

    }
};

int main()
{
    Solution s;
    string x = "testtesttest";
    cout<<s.repeatedSubstringPattern(x)<<endl;
    return 0;
}