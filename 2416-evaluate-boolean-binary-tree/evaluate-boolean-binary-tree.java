/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean evaluateTree(TreeNode root) {
        return rec(root);
    }
     private boolean rec(TreeNode root) {
        if (root.left == null && root.right == null) {
            return root.val != 0;
        }
        boolean l = rec(root.left);
        boolean r = rec(root.right);
        boolean ans = false;
        if (root.val == 2) {
            ans = l || r;
        }
        if (root.val == 3) {
            ans = l && r;
        }
        return ans;
    }
}