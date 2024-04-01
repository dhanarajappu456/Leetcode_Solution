import math as m 

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if nums ==[1]:
            return True
        nums  = set(nums)
        
        if 1 in nums:
            return False
        

        fact =  defaultdict(list)
        adj = defaultdict(set)
        for num in nums:
            for f in range(1,int(m.sqrt(num)+1)):
                if num%f ==0:

                    if f != 1:
                        if fact[f]:
                            adj[fact[f][-1]].add(num)
                            adj[num].add(fact[f][-1])
                        fact[f].append(num)
                    if fact[num//f]:
                        adj[fact[num//f][-1]].add(num)
                        adj[num].add(fact[num//f][-1])    
                    fact[num//f].append(num)
        vis  = set()
        def dfs(num):
            vis.add(num)
            for neib in adj[num]:
                if neib not in vis:
                    dfs(neib)

        cnt  = 0
        for num in nums:
            if num not in vis:
                if cnt ==1:
                    return False
                dfs(num)
                cnt+=1
        return True