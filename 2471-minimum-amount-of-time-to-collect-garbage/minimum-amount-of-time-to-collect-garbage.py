'''
simple direct approach 
the total time is sum of time taken  all type of truck just to travel  and total time spent at collecting


1) to calculate total collecting time,

 we need to find last house where the particular garbage is present , 
based on which the truck has to travel that long and hence the cost 
2) to calculate the time for whole collection
since it each unit take 1 min, tot time is  sum of length of each assortment in each house

'''

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(travel)
        prefix_travel_cost = [0 for i in range(n)]
        prefix_travel_cost[0]= travel[0]

        
        for i in range(n):
            if i>=1 :   
                prefix_travel_cost[i] =prefix_travel_cost[i-1]+travel[i]
       
        tot_travel_time =0
        g_last_house, m_last_house, p_last_house =0,0,0

        for i in range(len(garbage)):
            g = garbage[i] 
            tot_travel_time +=(len(g))
            for type_ in g:
                if type_  =="G":
                    g_last_house = i
                elif type_ == "M":
                    m_last_house = i
                else:
                    p_last_house = i
       
        collecting_time =0 
        collecting_time += prefix_travel_cost[g_last_house-1] if g_last_house-1>=0 else 0
        collecting_time += prefix_travel_cost[m_last_house-1] if m_last_house-1>=0 else 0
        collecting_time += prefix_travel_cost[p_last_house-1] if p_last_house-1>=0 else 0
      
        return tot_travel_time + collecting_time



               
        

