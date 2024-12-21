# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def rec(root):
            if root  == None:
                return 0
            l = rec(root.left)
            r = rec(root.right)
            print(l,r)
            self.ans = max(self.ans , l-1, r-1)

            if (root.left and root.left.val == root.val)  and ( root.right and root.right.val == root.val ):
                self.ans = max( self.ans , l +r +1)
                return max(l,r)+1
            if root.left and( root.left.val == root.val):
                self.ans = max( self.ans , l +1 )
                return l+1
            if root.right and (root.right.val == root.val):
                self.ans = max( self.ans ,r +1 )
                return r+1
            return 1
        #self.ans  = max( self.ans ,rec(root)-1)
        
        ans = rec(root)


        return max(0,self.ans-1)
       