'''

the idea is we find answer for root here 0 
then if you observe when we have ans for parent then ans for child can be found 
such that 
y = a -x + (n-x)
where 
y =ans_for_current_node
a = ans_for_parent 
x = total_number_of_nodes in subtree_of_current_node inclusing current node(1 is reduced from each subtree node,as compared
to that of parent)
(n-x) = remaining number of nodes(1 is increased for each other noded as compared to that of parent)


this formula can be derived / obtained if you draw some examples

t n

s n(aux space)+ n(count space)

'''

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj  =defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        count =[ 0 for i in range(n)]
        ans =  [0 for i in range(n)]
        #count number of nodes in subtree of a node, including the node
        vis  = set()
        def rec1(root):

            if root == None: 
                return 0
            vis.add(root)
            res =0 
            for nb in adj[root]:
                if nb not in vis:
                    res+=rec1(nb)
            count[root] = 1+res
            return count[root]
        #find the ans for root 

        def rec2(root,depth):
            if root == None:
                return 
            res = 0 
            vis.add(root)
            for nb in adj[root]:
                if nb not in vis:
                    res+=rec2(nb,depth+1)
            return depth + res
        
        #find the ans for all nodes

        def rec3(root,par):
            if root == None:
                return 
            vis.add(root)
            if par!=-1:
                
                ans[root] = ans[par] - count[root] + n-count[root]
            
            
            for nb in adj[root]:
                if nb not in vis:
                    rec3(nb,root)
        
        vis = set()
        rec1(0)
        vis = set()
        res = rec2(0,0)
        ans[0] =res
        vis = set()
        rec3(0,-1)

        return ans

        




        