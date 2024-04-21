# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
       
        def dfs(root,par,grand):
            if root == None:
                return 0 
            
            s = 0
            l  =dfs(root.left,root,par) 
            r = dfs(root.right,root,par)

            if grand!=None and grand.val%2==0:
                s= root.val
            
            return l+r+s
        return dfs(root,None,None)
                
            

            


        