# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # remember the stinf is constructed from bottom to top
        #t =n 
        #s = n 
        def rec(root,string):
            # neglect this time complexity
            string = chr(97+root.val)  + string
            if root.left and root.right:
                return min(rec(root.left,string), rec(root.right,string))
            if root.left:
                return rec(root.left,string)
            
            if root.right:
                return rec(root.right,string)
            return string
        return rec(root,"")
      
            
                

        