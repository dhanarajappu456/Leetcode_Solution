
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def rec(root):
            if root == None:
                return 
            rec(root.left)
            arr.append(root.val)
            rec(root.right)
        rec(root)
        print(arr)
        def rec(i,j):
            if i>j:
                return  None
            m_ind = (i+j)//2
            l = rec(i,m_ind-1)
            r = rec(m_ind+1,j)
            node  = TreeNode(arr[m_ind])
            node.left  = l
            node.right = r
            return node
        return rec(0,len(arr)-1)


        
        