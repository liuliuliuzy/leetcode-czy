var largest1BorderedSquare = function(grid) {
    var gird = grid
    var row = grid.length
    var col = grid[0].length
    var res = 0
    function maxRight(i, j){
        console.log(i, i)
        let cal = 0
        while(j < col){
            if(gird[i][j]){
                cal += 1
                j += 1
            }
            else{
                break
            }
        }
        return cal
    }
    function maxDown(i, j){
        let cal = 0
        while(i < row){
            if(gird[i][j]){
                cal += 1
                i += 1
            }
            else{
                break
            }
        }
        return cal
    }
    for(let i=0; i<row; i++){
        for(let j=0; j<col; j++){
            if(gird[i][j] == 0){
                continue
            }
            // console.log(maxRight(i, j), maxDown(i, j))
            let scale = Math.min(maxRight(i, j), maxDown(i, j))
            for(let k=scale-1; k>=0; k--){
                if(maxRight(i+k, j) < k+1){
                    continue
                }
                if(maxDown(i, j+k) < k+1){
                    continue
                }
                res = Math.max(res, k+1)
                break
            }
        }
    }
    return res*res
};
var grid = [[1, 1], [1, 0]]
console.log(largest1BorderedSquare(grid))
console.log(grid)