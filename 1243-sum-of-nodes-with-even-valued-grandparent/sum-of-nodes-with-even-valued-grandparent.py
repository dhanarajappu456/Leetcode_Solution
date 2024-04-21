'''
solution - 1
dfs 
note the problem asks to sum nodes with even value as grand parent, not nodes with even greandparent and grangrandparent 
and so on...
just one level grand parent need to be taken into account
just keep track of the parent and grandparent details for each node, to verify if node's value 

be added  to the sum
t  n
s  n

'''
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
       
        def dfs(root,par,grand):
            if root == None:
                return 0 
            
            s = 0
            l  =dfs(root.left,root,par) 
            r = dfs(root.right,root,par)

            if grand!=None and grand.val%2==0:
                s= root.val
            
            return l+r+s
        return dfs(root,None,None)
                
            

            


        