# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = [ ]
        ans = []
        while(stk or root):
            while(root):
                stk.append(root)
                root = root.left
            top  = stk.pop()
            ans.append(top.val)
            if top.right:
                root = top.right
        return ans
            
        