class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)
        if n < (m*k):
            return -1
    
        
        
        
        def possible(curr_day):
            boq_rem  =m 
            i=0
            while((i<n) and boq_rem):
                flow_rem = k
                j =i
                while(j<n and bloomDay[j]<=curr_day and flow_rem):
                    flow_rem-=1  
                    j+=1
                if flow_rem==0:
                    boq_rem-=1
                    i=j
                else:
                    i=j+1
            print(curr_day,boq_rem)
            return  boq_rem ==0
                
            
        l,r =1,max(bloomDay)
        ans = -1
        while(l<=r):
            
            d  = (l+r)//2
            if possible(d):
                ans  = d
                r=d-1
            else:
                l=d+1
                
        return ans

                
                    
                
                    
                    

        
        