# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        

        def rec(root):

            if root  == None:
                return float("inf")
            if root.left == None and root.right == None:
                return  1
            

            return min(rec(root.left) , rec(root.right))+1
        ans  = rec(root)
        return 0  if ans   == float("inf") else ans