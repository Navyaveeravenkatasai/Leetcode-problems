/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool checkTree(TreeNode* root) {
        if(root==NULL || (!root->left && !root->right)){
            return true;
        }
        int leftdata=0,rightdata=0;
        if(root->left){
            leftdata=root->left->val;
        }
        if(root->right){
            rightdata=root->right->val;
        }

        if(leftdata+rightdata == root->val){
            return true;
        }
        else{
            return false;
        }
    }

};