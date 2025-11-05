# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk =  []
        if root != None:
            stk.append(root)
        ans = []
        while(stk):

            root =stk.pop()
            ans.append(root.val)
            if root.right!=None:
                stk.append(root.right)
            if root.left!=None:
                stk.append(root.left)
        return ans
