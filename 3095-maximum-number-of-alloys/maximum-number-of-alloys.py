class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        




        def canCreate(units):
            # remember we have to use the same machine , for creating all the units
            for machine in range(k):
                totCost =  0
                for metal in range(n):
                    totCost+= (max(0,(composition[machine][metal]*units - stock[metal]))*cost[metal])
               
                if totCost <= budget:
                   
                    return True
            return False



        ans = 0
        l,h = 0, 2*(10**8)
        while(l<=h):
            m  = (l+h)//2
            if canCreate(m):
                ans  = m
                l = m +1
            else:
                h =m-1
        return ans