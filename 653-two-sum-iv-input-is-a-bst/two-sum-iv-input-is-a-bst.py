# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        stk1 = []
        stk2  = []

        temp = root
        while(temp): 
            stk1.append(temp )
            temp = temp.left 
            
        temp  = root
        while(temp):
            stk2.append(temp) 
            temp = temp.right 
            

        def next():

            nd = stk1.pop(-1)
            temp = nd.right
            while(temp):
                stk1.append(temp)
                temp  = temp.left
            return nd
        def before():
            nd = stk2.pop(-1)
            temp = nd.left
            while(temp):
                stk2.append(temp)
                temp  = temp.right
            return nd
        
        i,j = next(),before()
        while(i!=j):

            if i.val + j.val > k:
                j = before()
            elif i.val + j.val <k:
                i = next()
            else: 
                return True
        return False


