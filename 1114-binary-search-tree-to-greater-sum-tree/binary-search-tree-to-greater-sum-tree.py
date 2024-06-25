# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:


        def rec(root,s):
            if root == None:
                return 0
            old_val  = root.val
            r = rec(root.right,s)
            root.val = root.val + s +r 
            l = rec(root.left,root.val)

            return old_val + l+ r 
        rec(root,0)
        return root