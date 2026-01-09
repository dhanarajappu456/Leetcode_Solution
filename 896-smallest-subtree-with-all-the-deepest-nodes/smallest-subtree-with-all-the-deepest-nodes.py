# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        


        def dfs(root):


            if root == None:
                return 0 
            return( max(dfs(root.left)   , dfs(root.right)) + 1)
        
        d = dfs(root)


        def rec(root, curr_d):

            if root == None:
                return None
            if d == curr_d:
                return root
            left   = rec(root.left, curr_d+1)
            right  = rec(root.right, curr_d +1)
            if left and right:
                return root
            return left or right
        return rec(root, 1)


        

