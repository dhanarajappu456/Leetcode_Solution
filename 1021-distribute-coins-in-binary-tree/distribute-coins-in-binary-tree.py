'''
    we do a post order traversal here
    idea is , each excess coin has to move/transact somewhere and also each deficient coin for a node need to be 
    brought from somewhere, also it is said coin sum is == total nodes, so no other headaches.
    so , what we do,  when at a node , we check if we take a coin from all excess coins(+ if excess and -ve if already
    
    deficient) from left and right + current root's coin, and return the net remaining coin , 
    
    note : these value abs(l)+ abs(r) + root.val-1 , is nothing but coin that need to be sufficed/ by some nodes/ or moved
    to some other nodes for sufficing. which is the answer added to ans variable.
    

    which is added to ans at each node visited
'''
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def rec(root):
            nonlocal ans
            if root == None:
                return  0 
            l = rec(root.left)
            r = rec(root.right)
            ans += abs(l)+abs(r)
            return l+r+root.val-1
        rec(root)
      
        return ans

        