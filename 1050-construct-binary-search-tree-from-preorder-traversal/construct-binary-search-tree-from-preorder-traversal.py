# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        

        def rec(root,upper):

         
            if preorder == [] or preorder[0]>= upper:
                return None
            else:
                root = TreeNode(preorder.pop(0)) 

            root.left = rec(root.left,root.val)
            root.right  = rec(root.right,upper)
            return root
        return rec(preorder, float("inf"))