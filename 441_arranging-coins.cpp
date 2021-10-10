#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

class Solution {
public:
    int arrangeCoins(int n) {
        int ans = 0;
        int row = 1;
        while (n > 0) {
            n -= row;
            row ++;
            if (n >= 0) {
                ans++;
            }
        }
        return ans;
    }
};

int main()
{
	Solution s;
	for(int i=1; i<24; i++){
		cout<<i<<" "<<s.arrangeCoins(i)<<endl;
	}
	return 0;
}