class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        #queris and items sorted on price
        #note that we need to presereve the old index of he query 
        #when sorting so that when we cget the answer for current 
        #price we look , we ned to know , in which index we need to 
        #store this ans 
        queries =[(p,i) for i,p in enumerate(queries)]
        items  = [(p,b) for p,b in items ]
        queries.sort()
        items.sort()
        len_items  = len(items)
        len_queries = len(queries)
        #final res array 
        res = [0 for i in range(len_queries)]
        j= 0
        ans = 0
        #we start processing the queries , which is 
        #sorted on price.
        for p,ind_old in queries:
            #for current query price , we 
            #resume traversing the sorted items array
            #until the prices are <=the current query price
            #while doing this find max beauty so far
            while(j<len_items and items[j][0]<= p):
                ans = max(ans, items[j][1])
                j+=1 
            #once we get the beauty so far store it under 
            #current query index poation in the old query aray
            res[ind_old] = ans 
        return res 





        

        
        