# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:


        '''
            
            1.create the undirected greaph 
            2.Find and store  leaf node
            3.for each leaf node find the pair by starting bfs
        
        '''
        

        
        adj = defaultdict(list)

        leafs  = set()

        '''
        create undir graph
        '''
        def create_g(root,prev):
            if root == None:
                return None 
            if root.left  == None and root.right == None:
                leafs.add(root)
            if prev!= None:
                adj[root].append(prev)
                adj[prev].append(root)
            create_g(root.left,root)
            create_g(root.right,root)
        create_g(root,None)

        '''
        to keep track of processed leafs, means all pair with this leaf is obtained
        '''
        processed_leaf  =  set()
        ans = 0

        '''
        processing each leaf , 
        by starting bfs from this leaf  till d dist frontier , 
        so as  to find all the valid pair formed by this leaf
        '''
        for leaf in leafs:
            d=1 
            q= deque([])
            if leaf not in processed_leaf:
                q = deque([leaf])
            
            vis = set()
            
            vis.add(leaf)
            while(d<=distance):
                size = len(q )
                for i in range(size):
                    node = q.popleft( )
                    for neib in adj[node]:
                        
                        if neib not in vis:
                            q.append( neib )
                            vis.add( neib )
                            '''
                            got other node of the valid pair with leaf
                            '''
                            if neib not in processed_leaf  and neib.left  == None and neib.right == None:
                                ans+=1
                d+=1
            processed_leaf.add(leaf)
        return ans




        