class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        

        res=[]
        for curr in intervals:
            
            
            if  curr[ 1] < newInterval[0]:
                
                res.append(curr)
            elif  newInterval[1]<curr[0]:
                res.append(newInterval)
                newInterval = curr
            else:
                
                newInterval = [min(newInterval[0], curr[0] ) , max(newInterval[1],curr[1])] 
              
        res.append(newInterval)
        return res
        