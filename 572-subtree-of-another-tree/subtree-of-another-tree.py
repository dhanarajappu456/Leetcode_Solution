class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # remember preorder / postorder with null values included in the serialization, is unique

        def pre_order(root, res):
          
            if root == None :
                res.append("-n")
                return res
            
            # we need to use the delimiter in between the values to avoid incorrect answer for edge case like 
            # eg: if we don't use the delimiter :
            # root = 12 , ser = n12n 
            # subroot  = 2  ser = n2n
            # which says subroot is subtree of tree, but actually is not
            res.append("-"+str(root.val))

            pre_order(root.left, res)
            pre_order(root.right, res)

            return res

        ser1 = pre_order(root, [])
        ser2 = pre_order(subRoot, [])
        
        # converting to string , for using the string matching later
        ser1, ser2  = "".join(ser1) , "".join(ser2)

        # assume this string matching like kmp
        ans  = ser1.find(ser2)
        # if ans == -1:
        #     return False
        # return True
        if ser2 in ser1:
            return True
        return False

            

#t   :o(m+n)
#s :  o(m) +o(n)