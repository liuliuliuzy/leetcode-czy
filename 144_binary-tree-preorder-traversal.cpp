#include <vector>

using namespace std;
//  * Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    // Recursive version
    void helper (TreeNode* root, vector<int> &res){
        if(!root) return ;
        // 调整对当前节点的操作语句放置的位置，即可分别完成二叉树的前/中/后序遍历
        res.push_back(root->val);
        helper(root->left, res);
        helper(root->right, res);
    }
    // Iteration version
    vector<int> mapAllNodes(TreeNode* root){

    }
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        helper(root, res);
        return res;
    }
};

