
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def rec(p1,p2):

            if p1  == None or p2==None:
                return p1==p2
            
            if p1.val == p2.val:
                return (rec(p1.left,p2.left ) or rec(p1.left, p2.right) )and (rec(p1.right,p2.right) or rec(p1.right, p2.left ) )
            else:
                return False
            
        return rec(root1,root2)