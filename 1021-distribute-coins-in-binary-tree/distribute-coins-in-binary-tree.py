# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def rec(root):
            nonlocal ans
            if root == None:
                return  0 

            l = rec(root.left)
            r = rec(root.right)
            ans += abs(l)+abs(r)
          
            return l+r+root.val-1
        rec(root)
      
        return ans

        