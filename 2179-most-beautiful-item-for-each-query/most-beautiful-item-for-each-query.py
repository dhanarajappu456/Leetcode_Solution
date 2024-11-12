class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        queries =[(p,i) for i,p in enumerate(queries)]
        queries.sort()
        items  = [(p,b) for p,b in items ]
        items.sort()
        len_items  = len(items)
        len_queries = len(queries)
        res = [0 for i in range(len_queries)]
        j= 0
        ans = 0
        for p,ind_old in queries:
            while(j<len_items and items[j][0]<= p):
                ans = max(ans, items[j][1])
                j+=1 
            res[ind_old] = ans 
        return res 





        

        
        