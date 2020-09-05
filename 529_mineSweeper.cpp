#include <cstdio>
#include <vector>
#include <iterator>

using namespace std;

//来自Lzy的dfs，慢的一逼...
class Solution {
public:
    int hasMineNeighbor(vector<vector<char>>& board, int row, int col, int maxRow, int maxCol){
        int flag = 0;
        int dis[8][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}, {1, 1}, {-1, 1}, {-1, -1}, {1, -1}};
        for(auto item: dis){
            if(row+item[0]<0 || row+item[0]>=maxRow || col+item[1]<0 || col+item[1]>=maxCol){
                continue;
            } else {
                flag += (board[row+item[0]][col+item[1]] == 'M' ? 1 : 0);
            }
        }
        return flag;
    }
    void help(vector<vector<char>>& board, int row, int col, int maxRow, int maxCol){
        //如果挖到地雷
        if(board[row][col] == 'M'){
            board[row][col] = 'X';
        } else {
            int res = hasMineNeighbor(board, row, col, maxRow, maxCol);
            printf("%d\n", res);
            if(res){//如果周围存在地雷
                board[row][col] = (char)(res+48);
            } else {//如果周围没有地雷
                board[row][col] = 'B';
                int dis[8][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}, {1, 1}, {-1, 1}, {-1, -1}, {1, -1}};
                for(auto item: dis){
                    int newRow = row+item[0];
                    int newCol = col+item[1];
                    // printf("%s %d %d %d %d %d\n", "ready to recursive", newRow, newCol, maxRow, maxCol, 0<=newRow && newRow<maxRow && 0<=newCol && newCol<maxCol && board[newRow][newCol] == 'E');
                    if(0<=newRow && newRow<maxRow && 0<=newCol && newCol<maxCol && board[newRow][newCol] == 'E'){
                        printf("%s %d %d\n", "recursive", newRow, newCol);
                        help(board, newRow, newCol, maxRow, maxCol);
                    }
                }
            }
        }
    }
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        help(board, click[0], click[1], board.size(), board[0].size());
        return board;
    }
};


int main()
{
    Solution x;
    // char data[4][5] = {{'E','E','E','E','E'}, {'E','E',"M",'E','E'}, {'E','E','E','E','E'}, {'E','E','E','E','E'}};
    // vector<vector<char>> mine(begin(data), end(data));
    vector<vector<char>> mine = {
        {'E','E','E','E','E'}, 
        {'E','E','M','E','E'}, 
        {'E','E','E','E','E'}, 
        {'E','E','E','E','E'}
    };
    vector<int> click = {3, 0};
    for(int i=0; i<mine.size(); i++){
        for(int j=0; j<mine[0].size(); j++){
            printf("'%c' ", mine[i][j]);
        }
        printf("%c", '\n');
    }
    x.updateBoard(mine, click);
    for(int i=0; i<mine.size(); i++){
        for(int j=0; j<mine[0].size(); j++){
            printf("'%c' ", mine[i][j]);
        }
        printf("%c", '\n');
    }
    return 0;
}