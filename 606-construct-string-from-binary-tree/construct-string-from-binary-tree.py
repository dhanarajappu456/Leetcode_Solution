'''
When such question is got , 

remeber we need to distinuguish b/w  
t1: 2 null 4  
t2: 2 4 null
and the expected ans is 
for t1 : 2()(4)
for t2 : 2(4)

that is any children of node is assumed to be left then right , so left need to be always present 
in the string format 

that is if left subtree is empty  and right subtree exist for a node, left is represented by a ()


rest is just a recursion 

t n 
s n




'''
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:


        

        def rec(root):
            
            if root == None:
                return ""
           
            l =rec(root.left)
            r= rec(root.right)
            if l =="" and r!="":
              l = "()"
          
            return "(" +str(root.val)+ l+r +")"

        return rec(root)[1:-1]
            

