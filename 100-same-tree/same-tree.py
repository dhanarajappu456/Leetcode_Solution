
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (self.rec(p,q))
    
    def rec(self,p,q):
        if p==None and q==None:
            return True
        if(p==None or q==None ):
            return False
        if p.val == q.val:
            return(self.rec(p.left,q.left) and self.isSameTree(p.right,q.right))
        
        
        
        
        
        