class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        


    
        #binserch on the units, cheking if the budget is possible or not
        
        def canCreate(units):
            # remember we have to use the same machine , for creating all the units
            for machine in range(k):  #k
                totCost =  0
                for metal in range(n): #n
                    totCost+= (max(0,(composition[machine][metal]*units - stock[metal]))*cost[metal])
               
                if totCost <= budget:
                   
                    return True
            return False



        ans = 0
        l,h = 0, 2*(10**8)
        while(l<=h):     #const c 
            m  = (l+h)//2
            if canCreate(m):
                ans  = m
                l = m +1
            else:
                h =m-1
        return ans

        #t  = c*k*n  = 10^4  *c  = 10^5(c of order of 10)