var dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
// var dfs = function(mat, i, j, memory){
//     if(memory[i][j]!=0) return memory[i][j]
//     memory[i][j]++
//     for(let k=0; k<4; k++){
//         let newI = i+dirs[k][0], newJ = j+dirs[k][1]
//         if(0<=newI<=rowScale && 0<=newJ<=colScale && mat[newI][newJ]>mar[i][j]){
//             memory[i][j] = Math.max(memory[i][j], dfs(mat, newI, newJ, memory)+1)
//         }
//     }
//     return memory[i][j]
// }

var longestIncreasingPath = function(matrix) {
    if(matrix.length == 0 || matrix[0].length == 0) return 0
    var rowScale = matrix.length, colScale = matrix[0].length
    var res = 0
    //initiate memory array
    var memory = new Array(rowScale)
    for(let i=0; i<rowScale; i++){
        memory[i] = new Array(colScale)
        for(let j=0; j<colScale; j++){
            memory[i][j] = 0
        }
    }
    function dfs(mat, i, j, memory) {
        if(memory[i][j]!=0) return memory[i][j]
        memory[i][j]++
        for(let k=0; k<4; k++){
            let newI = i+dirs[k][0], newJ = j+dirs[k][1]
            if(newI>=0 && newI<rowScale && newJ>=0 && newJ<colScale && mat[newI][newJ]>mat[i][j]){
                memory[i][j] = Math.max(memory[i][j], dfs(mat, newI, newJ, memory)+1)
            }
        }
        return memory[i][j]
    }
    for(let i=0; i<rowScale; i++){
        for(let j=0; j<colScale; j++){
            res = Math.max(res, dfs(matrix, i, j, memory))
        }
    }
    return res
};
var mat = [[9,9,4],[6,6,8],[2,1,1]]
console.log(longestIncreasingPath(mat))