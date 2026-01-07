# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        final_max = -float("inf")

        def dfs(root):

            if root == None:
                return 0
            a= dfs(root.left)
            b = dfs(root.right)

            return root.val + a +b
        

        tot_sum = dfs(root)

        def traversal(root):
            nonlocal final_max
            if root == None:
                return 0

            a = traversal(root.left)
            b = traversal(root.right)
            current_sum = a+b+root.val
            final_max = max(final_max , (tot_sum- current_sum)  * current_sum)
            return current_sum 
        traversal(root)
        mod = 10**9+7
        return final_max % mod 
        

        