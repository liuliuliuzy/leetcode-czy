#include "basicInclude.h"

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        string str[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> res;
        int length = digits.size();
        if(length == 0) return res;
        for(int i=0; i<length; i++){
            //如果res是空，那么将数字对应字符串的每一位字符加入
            if(res.size() == 0){
                string tmp = str[digits[i]-50];
                int tmp_len = tmp.size();
                for(int j=0; j<tmp_len; j++){
                    string chara(1, tmp[j]);
                    res.push_back(chara);
                }
            }
            //如果res不为空，那么将数字对应字符串的每一位字符加在res中每个字符串的后面
            else{
                int res_len = res.size();
                vector<string> tmp_res;
                string tmp = str[digits[i]-50];
                int tmp_len = tmp.size();
                for(int k=0; k<res_len; k++){
                    for(int l=0; l<tmp_len; l++){
                        string tmp_chara(1, tmp[l]);
                        string tmp_str = res[k] + tmp_chara;
                        tmp_res.push_back(tmp_str);
                    }
                }
                res.assign(tmp_res.begin(), tmp_res.end());
            }
        }
        return res;
    }
};