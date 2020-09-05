/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    if(board.length < 3 || board[0].length < 3){
        return
    }
    function bfs(i, j){
        var stack = new Array()
        stack.push([i,j])
        while(stack.length){
            let [I, J] = stack.pop()
            flags[I][J] = true
            if((I+1)<board.length && !flags[I+1][J] && board[I+1][J] == 'O'){
                stack.push([I+1, J])
            }
            if((I-1)>=0 && !flags[I-1][J] && board[I-1][J] == 'O'){
                stack.push([I-1, J])
            }
            if((J+1)<board[0].length && !flags[I][J+1] && board[I][J+1] == 'O'){
                stack.push([I, J+1])
            }
            if((J-1)>=0 && !flags[I][J-1] && board[I][J-1] == 'O'){
                stack.push([I, J-1])
            }
        }
    }
    //initial array
    var flags = new Array()
    for(let i=0; i<board.length; i++){
        flags[i] = new Array()
        for(let j=0; j<board[0].length; j++){
            flags[i][j] = false
        }
    }
    var dirs = new Array()

    for(let i=0; i<board[0].length-1; i++){
        dirs.push([0, 1])
    }
    for(let i=0; i<board.length-1; i++){
        dirs.push([1, 0])
    }
    for(let i=0; i<board[0].length-1; i++){
        dirs.push([0, -1])
    }
    for(let i=0; i<board.length-1; i++){
        dirs.push([-1, 0])
    }
    console.log(dirs)
    var i=0, j=0
    for(let k=0; k<dirs.length; k++){
        console.log("now", i, j)
        if(board[i][j] == 'O' && !flags[i][j]){
            bfs(i, j)
        } else {
            flags[i][j] = true
        }
        i+=dirs[k][0]
        j+=dirs[k][1]
    }
    for(let i=1; i<board.length-1; i++){
        for(let j=1; j<board[0].length; j++){
            if(board[i][j] == 'O' && !flags[i][j]){
                board[i][j] = 'X'
            }
        }
    }
};

// var board = [['X', 'O', 'X', 'X', 'O'], ['O', 'O', 'O', 'X', 'O'], ['O', 'X', 'X', 'O', 'X'], ['X', 'X', 'X', 'X', 'O'], ['O', 'O', 'O', 'X', 'O']]
var board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
console.log(board)
solve(board)
console.log(board)