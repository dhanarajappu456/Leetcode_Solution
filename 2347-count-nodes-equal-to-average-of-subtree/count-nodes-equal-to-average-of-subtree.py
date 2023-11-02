# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        ans =0
      
        def rec(root):
            if root ==None:
                return (0,0)
            nonlocal ans 
            l_sum , l_count = rec(root.left)
            r_sum,r_count = rec(root.right)
            if math.floor((l_sum+r_sum+root.val) / (l_count + r_count+1)) == root.val:
                ans+=1
            return (l_sum+r_sum+root.val,l_count + r_count+1 )
        rec(root)
        return ans



        