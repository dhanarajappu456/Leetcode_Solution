class DSU:

    def __init__(self,n):

        self.par =[i for i in range(n)]
        self.rank=[1 for i in range(n)]



    
    def findPar(self,u):
        
        if self.par[u] ==u:
            return u

        self.par[u] = self.findPar(self.par[u])
        return self.par[u]


    def union(self,u,v):


        pu,pv = self.findPar(u),self.findPar(v)
        if self.rank[pu]<self.rank[pv]:
            self.par[pu] = pv 
        elif self.rank[pu]>self.rank[pv]:
            self.par[pv] = pu
        else:
            self.par[pu] = pv
            self.rank[pv]+=1
    




class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

       
        ds_alice = DSU(n)
        ds_bob   = DSU(n)
        edges.sort(key = lambda x:-x[0])
        cnt =0
        for t,u,v in edges:
            u-=1 
            v-=1
            
            if  t==1:
                p1 = ds_alice.findPar(u)
                p2 = ds_alice.findPar(v)
                
                if p1==p2:
                    cnt+=1
                else:
                    ds_alice.union(p1,p2)


                

            elif t==2:
                p1 = ds_bob.findPar(u)
                p2 = ds_bob.findPar(v)
                
                if p1==p2:
                    cnt+=1
                else:
                    ds_bob.union(p1,p2)
                    

            else: 
                
                p1 = ds_alice.findPar(u)
                p2 = ds_alice.findPar(v)
                p3 = ds_bob.findPar(u)
                p4 = ds_bob.findPar(v)
                if p1==p2 or   p3==p4:
                    cnt+=1
                else:
                    ds_alice.union(p1,p2)
                    ds_bob.union(p1,p2)

               
        
        alice_pars, bob_pars =set() , set()
        for p in range(n):
            p =p-1
            alice_pars.add(ds_alice.findPar(p))
            bob_pars.add(ds_bob.findPar(p))
        # checking if there is only one component at , end
        #meaning that every node can be traversed by both alices and bob
        if len(alice_pars) == len(bob_pars) ==1 :
            return cnt
        return -1 

        
                


                
                
        
