# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def rec(root):

            if root  == None:
                return None
            l   = rec(root.left)
            r =  rec(root.right)
            root.left = l
            root.right = r 
            
            if low<=root.val<=high:
    
                return root
            return l or r

        return rec(root)

        

      
            



