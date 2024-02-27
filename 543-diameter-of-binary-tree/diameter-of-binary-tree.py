# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_=0
        self.rec(root)
        return self.max_
    def rec(self,node):
        if not node:
            return 0
        left = self.rec(node.left)
        right = self.rec(node.right)
        self.max_=max(self.max_,left+right)
        return max(left,right)+1