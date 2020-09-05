/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    if(prerequisites.length == 0){
        return true
    }
    var dict = {}
    var flag = false
    for(let i=0; i<prerequisites.length; i++){
        if(dict[prerequisites[i][0]] == undefined){
            dict[prerequisites[i][0]] = [prerequisites[i][1]]
        }else{
            dict[prerequisites[i][0]].push(prerequisites[i][1])
        }
    }
    console.log(dict)
    var marked = {}
    for(let key in dict){
        if(marked[key]==undefined){
            // console.log("key: ", key)
            let res = DFS(key, marked)
            if(flag) return false
        }
    }
    return true
    //then we got a linked list
    function DFS(v, marked){
        console.log("tes", v)
        if(flag) return
        marked[v] = false
        var adj = dict[v]
        for(index in adj){
            if(marked[adj[index]] == undefined && adj[index]<numCourses){
                DFS(adj[index], marked)
            } else if(marked[adj[index]] == false && adj[index]<numCourses){
                flag = true
                return
            }
        }
        marked[v] = true
        // return true
    }
};
var limits = [[0,1], [2,0], [1,2], [1,3], [2,4], [3,4], [5,4], [5,6]]
console.log(canFinish(6, limits))