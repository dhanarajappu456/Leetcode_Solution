# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        first , second = float("inf") , float("inf")

        def rec(root):
            nonlocal first
            nonlocal second
            if root   == None:
                return float("inf")
            
            if root.val < first:
                second  = first
                first  = root.val
                
            
            elif( root.val < second) and( first != root.val ):
                second = root.val
           
            l= rec( root .left) 
            r = rec(root.right)
        rec(root)
        return second if second != float("inf") else -1

