#include "basicInclude.h"

class Solution {
public:
    void dfs(int room, vector<vector<int>>& rooms, set<int> &flags){
        if(flags.count(room)){
            return ;
        }
        flags.insert(room);
        for(auto key: rooms[room]){
            dfs(key, rooms, flags);
        }
    }
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        if(rooms.size() == 1){
            return true;
        }
        set<int> flags;
        dfs(0, rooms, flags);
        return flags.size()==rooms.size();
    }
};

int main()
{
    set<int> x;
    cout<<x.count(-1)<<endl;
    x.insert(-1);
    cout<<x.count(-1)<<endl;
    return  0;
}