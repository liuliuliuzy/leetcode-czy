/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
//recursive version
var isSameTree = function(p, q) {
    if(p==null && q==null) return true
    if(p==null || q==null) return false
    if(p.val != q.val) return false
    return isSameTree(p.left, q.left)&&isSameTree(p.right, q.right)
};

//stack version
var isSameTreeStackV = function(p, q){
    if (p == null && q == null) return true
    if (p == null) return false
    if (q == null) return false
    var stackP = []
    var stackQ = []
    while (p != null || q != null || stackP.length || stackQ.length) {
        if (p != null && q != null) {
            stackP.push(p)
            stackQ.push(q)
            p = p.left
            q = q.left
        } else if (q == null && p == null) {
            p = stackP.pop()
            q = stackQ.pop()
            if (p.val != q.val) {
                return false
            }
            p = p.right
            q = q.right
        } else {
            return false
        }
    }
    return true; 
}