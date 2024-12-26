
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.helper(root.left,root.right)
       
         
    def helper(self,n1,n2):
        if n1==None and n2==None :
            return True
        if n1 == None or  n2 == None:
            return False
        if n1.val!=n2.val:
            return False
        return (self.helper(n1.left,n2.right) and self.helper(n1.right,n2.left))               
                
        