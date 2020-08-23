/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 
class Solution {
public:
    int minDepth(TreeNode* root) {
        printf("is  %d\n", root->val);
        //如果首次输入的就是NULL
        if(root==NULL) return 0;
        //如果节点无左右子节点
        if(root->left==NULL && root->right==NULL){
            return 1;
        }
        //如果节点只有左/右子节点
        if(root->left==NULL || root->right==NULL){
            return 1 + (root->left==NULL ? minDepth(root->right) : minDepth(root->left));
        }
        //如果节点有左右子节点
        else{
            return 1+min(minDepth(root->left), minDepth(root->right));
        }
    }
};

int main()
{
    TreeNode root(1);
    TreeNode node(2);
    root.right = (TreeNode*)&node;
    printf("%d %d\n", root.val, root.right->val);
    Solution s;
    int res = s.minDepth(&root);
    printf("answer is %d\n", res);
    return 0;
}

//line 36，我一开始忘记写三元表达式外面的()...，导致segmentation fault，好久没写c++，我也是醉了