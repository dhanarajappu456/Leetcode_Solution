# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:


        

        def rec(root):
            
            if root == None:
                return ""

            l =rec(root.left)
            r= rec(root.right)
            if l =="" and r!="":
              l = "()"
            return "(" +str(root.val)+ l+r +")"

        return rec(root)[1:-1]
            

