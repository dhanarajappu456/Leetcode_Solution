# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        start , end  = None, None

        '''
        find lca 
        '''
        def lca_find(root):


            if root == None :
                return None 
            nonlocal start, end
            l= lca_find(root.left)
            r = lca_find(root.right)
            root_ = None
            if root.val == startValue or root.val == destValue or (l and r ):
                root_ = root 
                if  root.val == startValue:
                    start  = root
                if root.val   == destValue:
                    end   = root


            
            return root_ or l or r 
                


        '''

            `1. find path from lca to startValue
            2., find path from lca to  destValue`
        '''
        def path_find(s, d,path):
            if s  == None:
                return False
            if s == d:
                return True
            path.append("L")
            if path_find(s.left, d,path):
                return True
            path.pop()
            path.append("R")
            if path_find(s.right, d, path):
                return True
            path.pop()
            




        lca = lca_find(root)
        lca_to_src = []
        lca_to_dest =[]

        path_find(lca,start,lca_to_src)
        path_find(lca,end,lca_to_dest)

        ans = ""
     
        '''we need to change all the movement from lca to srcValue to "U"
        '''
        for c in lca_to_src:
            ans+="U"

        ans+= "".join(lca_to_dest)
        

        return ans




            

        