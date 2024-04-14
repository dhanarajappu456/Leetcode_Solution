# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

    
        def rec(root,is_left):
            if root == None:
                return  0
            #consider the root value iff it is a leaf node and is a left child
            elif root.left  == None and root.right == None and is_left:
                return root.val
            
            #in other case  just return value sum of l and r 
            l =   rec(root.left,1)
            r =   rec(root.right,0)

            return l+r
        
        return rec(root,0)
        