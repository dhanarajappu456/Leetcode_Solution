# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        def rec(root):
            if root  == None:
                return None
            a = rec(root.left)
            b = rec(root.right)
            root.left = b
            root.right = a
            return root
        return rec(root)
            