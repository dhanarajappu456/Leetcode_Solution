class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        seen=set()
        parent = self.level_order([root])
        dist =0
        qu=[target]
        while(dist!=k):
            size =len(qu)
            for i in range(size):        
                n = qu.pop(0)
                if n.left and n.left not in seen:
                    qu.append(n.left)
                if n.right and n.right not in seen:
                    qu.append(n.right)
                if n in parent and parent[n] not in seen:
                    qu.append(parent[n])
                seen.add(n)
            dist+=1
        return [i.val for  i in  qu]    
    def level_order(self,l):
        parent=dict()
        q=l
        while(q):
            size = len(q)
            for i in range(size):
                front = q.pop(0)
                if front.left :
                    parent[front.left]=front
                    q.append(front.left)
                if front.right:
                    parent[front.right]=front
                    q.append(front.right)
        return  parent            
    