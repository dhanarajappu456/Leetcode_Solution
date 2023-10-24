import java.util.Queue;
import java.util.List;
import java.util.LinkedList;

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
    public List<Integer> largestValues(TreeNode root) {

        List<Integer>  ans =  new ArrayList<Integer>();
        
        Queue<TreeNode> q=  new LinkedList<TreeNode>();
        if( root !=null) {
            q.offer(root);

        }

           
        int l ; 
        int max_val ;
        while(q.size()>0){

            l = q.size();
            max_val = Integer.MIN_VALUE;
           for(int  i = 0; i < l; i++) {

            TreeNode node = q.poll();
            max_val = Math.max(max_val, node.val);
            
            
            if (node.left!=null)
          
                q.offer(node.left);
            if ( node.right!=null)
              
                q.offer(node.right);
           }
           ans.add(max_val);

        } 
            

   return ans;
    }
 
}