# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        

        def rec(l,h):
            if l>h:
                return [None]
            
            ans  =[]
            for i in range(l,h+1):

                left = rec(l,i-1)
                right  = rec(i+1,h)

                for node_l in left:
                    for node_r in right:
                        node = TreeNode(i)

                        node.left = node_l
                        node.right = node_r

                        ans.append(node)
            return ans
            
        return rec(1,n)