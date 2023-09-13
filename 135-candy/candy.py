class Solution:
    def candy(self, ratings: List[int]) -> int:

        #sort the (rating , index)

        #process each of them in the sorted ordering 

        #when processing check if the neib value is less than than current value , 
        #then take in to account candies assigned to neibour  +1 

        arr = [(val,ind) for ind, val  in enumerate(ratings)]
        arr.sort()
        n =len(ratings)

        candies  =[0 for i in range(n)]

        for val,ind in arr:
            neib_cand =0
            if ind-1>=0 and ratings[ind-1]< ratings[ind]:
                neib_cand = max(neib_cand, candies[ind-1] )
            
            if ind+1<n and ratings[ind+1]< ratings[ind]:
                neib_cand = max(neib_cand, candies[ind+1] )
            
            candies[ind] = neib_cand+1
        return sum(candies)
            
