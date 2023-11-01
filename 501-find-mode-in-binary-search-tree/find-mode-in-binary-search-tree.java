class Solution {

    //note that we can;t use prev count and max as paramter in the rec method, 
    //rather use it as instance varibale , 
   // since     when processing a  root need updated prev ,count and max from its left child, whn inorder traversed.
   // not the value from the parent node
    int prev = 100000 + 1;
    int count = 0;
    int max = 0;
    List<Integer> ans = new ArrayList<Integer>();

    private void rec(TreeNode node) {

        if (node == null) {
            return;
        }
    
        rec(node.left);

        if (node.val == prev) {
            count++;
        } else {
            count = 1;
        }

        if (count == max) {
            ans.add(node.val);
        } else if (count > max) {
            ans.clear(); // Clear the list
            ans.add(node.val);
            max = count;
        }
        System.out.println(ans);
        prev = node.val;

        rec(node.right);
    }

    public int[] findMode(TreeNode root) {
        rec(root);
        int n = ans.size();
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = ans.get(i);
        }
        return res;
    }
}
