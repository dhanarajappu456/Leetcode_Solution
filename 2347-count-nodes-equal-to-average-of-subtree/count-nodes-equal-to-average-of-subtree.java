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
    int ans;
    private int[] rec(TreeNode root){

        if (root  == null){

            return new int[]{0,0};

        }

        int [] leftResult= rec(root.left);
        int [] rightResult = rec(root.right);

        int sum  =leftResult[0]+rightResult[0]+root.val ; 
        int count =  leftResult[1]+rightResult[1]+1;

        if( Math.floorDiv(sum,count) == root.val)
            ans++;

        return new int[]{sum, count};

    }
    public int averageOfSubtree(TreeNode root) {
        rec(root);
        return ans;
        
    }
}