/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
//I think it's DFS for binary tree and modify the tree
var flatten = function(root) {
    function helper(root){
        if(root == null) return null
        if(root.right){
            helper(root.right)
        }
        if(root.left){
            const leftFirst = helper(root.left)
            let leftLast = leftFirst
            while(leftLast.right){
                leftLast = leftLast.right
            }
            leftLast.right = root.right
            root.right = leftFirst
            root.left = null
        }
        return root
    }
    helper(root)
};

var test = function(root, stack = []) {
    if(!root)return 
    if(root.right){
        stack.push(root.right)
    }if(root.left){
        root.right = root.left;
        root.left = null;
        test(root.right,stack)
    }else{
        let node = stack.pop();
        root.right = node;
        root.left = null;
        test(root.right,stack)
    }
}

// var left = new TreeNode(2, 3, 4)
// var right = new TreeNode(5, null, 6)
// var root = new TreeNode(1, left, right)

var root = new TreeNode(1, null, null)
root.left = new TreeNode(2, null, null)
root.left.left = new TreeNode(3, null, null)
root.left.right = new TreeNode(4, null, null)
root.right = new TreeNode(5, null, null)
root.right.right = new TreeNode(6, null, null)

function Print(pRoot) {
    if (!pRoot) {
        console.log("test")
        return [];
    }
    var queue = [],
        result = [],
        flag = true;
    //头结点推入
    queue.push(pRoot);

    while (queue.length) {
        var len = queue.length;
        var tempArr = [];
        for (var i = 0; i < len; i++) {
            var temp = queue.shift();
            tempArr.push(temp.val);
            if (temp.left) {
                queue.push(temp.left);
            }
            if (temp.right) {
                queue.push(temp.right);
            }
        }
        if (!flag) {
            tempArr.reverse();
        }
        flag = !flag;
        result.push(tempArr);
    }
    return result;
}
console.log(Print(root))
flatten(root)
console.log(Print(root))
console.log(typeof(root))
