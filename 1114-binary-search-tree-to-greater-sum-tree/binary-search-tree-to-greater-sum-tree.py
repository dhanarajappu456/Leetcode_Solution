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
            if root.right == None:
                root.val = root.val + s 
                l = rec(root.left,root.val)
            else:
                r = rec(root.right,s)
                root.val += r 
                l = rec(root.left,root.val)
            return l or root.val
        rec(root , 0)
        return root