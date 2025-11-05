# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stk = [], []
        if root!=None:
            stk.append(root)

        while(stk):
            root = stk.pop()
            ans.append(root.val)
            if root.left:
                stk.append(root.left)
            if root.right:
                stk.append(root.right)
        return ans[::-1]
        