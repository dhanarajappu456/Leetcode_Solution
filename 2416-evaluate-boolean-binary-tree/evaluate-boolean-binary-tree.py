# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
       
        def rec(root):


            if (root.left  == None) and (root.right == None):
                return bool(root.val)
            l ,r  = rec(root.left),rec(root.right)
         
            if root.val ==2 :
                ans =  (l or  r)
            
            if root.val == 3:
                ans  = (l and  r)
            
            return ans
        
        return rec(root)

        