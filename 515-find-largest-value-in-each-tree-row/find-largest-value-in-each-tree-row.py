from collections import deque as dq
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        ans =  []

        def rec(root, lev):
            if root  == None:
                return None
            if len(ans)<lev:
                ans.append(root.val)
            else:
                ans[lev-1] = max(ans[lev-1], root.val)
            l = rec(root.left,lev+1)
            r = rec(root.right,lev+1)
        
        rec(root, 1)
        return ans

        
        