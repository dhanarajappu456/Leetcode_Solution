# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ans  =0 

        def rec(root):
            nonlocal ans 

            if root ==None:
                return 

            if root.val< low :
                rec(root.right)
            elif root.val>high:
                rec(root.left)
            else:
                print(root.val)
                ans+=root.val
                

                rec(root.left)
                rec(root.right)
            
        rec(root)
        return ans