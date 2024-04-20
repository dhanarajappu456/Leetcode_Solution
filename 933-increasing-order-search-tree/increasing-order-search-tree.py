#dfs 

#t n
#s n 
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
       
        def reform(root):
            if root == None:
                return None,None
            #left most node of right subtree , 
            #and right most node of right subtree
            r_left,r_right = reform(root.right)
            #left most node of left subtree and
            #right most node of left subtree
            l_left,l_right = reform(root.left)
            #if connect the right most node in the left subtree
            #to the root 
            if l_right:
                l_right.right = root
                root.left = None
            #make root.right point to 
            #left most  node of right subtree
            root.right = r_left
            return (l_left or root ),(r_right or root)
        l_left,r_right = reform(root)
        return l_left

        