# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #return self.rec(root,-1 * float('inf'),float('inf'))
        inorder =  [ ]
        
        def rec(root):
            
            if root  == None :
                return None

            rec(root.left)
            inorder.append(root.val)
            rec(root.right)
        
        rec(root)
        print(inorder)
        sorted_arr = sorted(inorder)
        if inorder != sorted_arr:
            return False
        #also there can be cases inorder  =[2,2,2]
        #in which case we need to return the false as the
        #answer
        for i in range(1,len(inorder)):
            if inorder[i-1] == inorder[i]:
                return False
        return True
       
    