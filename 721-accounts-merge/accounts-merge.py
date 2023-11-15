from collections import defaultdict as dict 
class DisjointSet:
    def __init__(self,V):
        self.rank = [1 for i in range(V)]
        self.parent = [i  for i in range(V)]
    #o(4*alpha) =O(1)
    def union(self,u,v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        if self.rank[pu] <self.rank[pv]:
            self.parent[pu] =pv    
        elif self.rank[pu] >self.rank[pv]:
            self.parent[pv] =pu
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
            
    
    def findParent(self,u):
        
        if self.parent[u]==u:
            return u
        #path compressed
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        ds = DisjointSet(len(accounts))
        emailToAccount = dict(int)
        for i in range(len(accounts)):
            acc = accounts[i]
            for email  in acc[1:]:
                if email in emailToAccount:
                    #merge to the ultimate parent of the account for which this email was first seen 
                    ds.union(i,emailToAccount[email])
                else:
                    emailToAccount[email] = i
        accToMails  = dict(list)         
        for email in emailToAccount :
            acc = emailToAccount[email]
            parAcc = ds.findParent(acc)
            accToMails[parAcc].append(email)
        
        res =[ ]
        for acc in accToMails:
  
            res.append([accounts[acc][0]]+sorted(accToMails[acc]))
        return res
                    
            
        