from collections import deque as dq
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
      
        ans = []
        q= dq([])
        if root !=None:

            q.append(root)
        print(q)
        while(q):

            l  = len( q)
            max_val = -math.inf
            for  i in range(l):
                node = q.popleft()
                max_val = max(max_val, node.val)
                
                
                if node.left:
                    l = node.left
                    q.append(l)
                if node.right:
                    r = node.right
                    q.append(r)
            ans.append(max_val)
        
        return ans

        
        