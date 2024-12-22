# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #return self.rec(root,-1 * float('inf'),float('inf'))
        inorder =  [ ]
        
        def rec(root,low,high):
            
            if root  == None:
                return True
            if not(low<=root.val<=high):
                return False
            l = rec(root.left,low,root.val-1)
            r =rec(root.right, root.val+1 , high)
            return l and r
        return rec(root,-float("inf"),float("inf"))

       
    