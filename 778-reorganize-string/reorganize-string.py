from collections import  defaultdict as dict
import heapq as h 
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        #create the map of char -> count
        map_  = self.createMapOfCharCount(s)
        arr = [(-1*map_[i],i)  for i in map_]
        res = []
        #maxheap , where key is the count of a characater
        h.heapify(arr)   
        while(arr):
            cnt,char  = h.heappop(arr)
            #if the character with the max count is the one selected last time, 
            #then not select it , look for next max characater in the heap
            if res and res[-1]==char:
                #look for second max occuring character
                if arr:
                    cnt2,char2  = h.heappop(arr)
                    res.append(char2)
                    cnt2+=1
                    if cnt2!=0:
                        h.heappush(arr,(cnt2,char2))
                #if the there is no second max character then return empty string , as the  required string can't be formed
                else:
                    return ""
            else:
                #if the current max character is not the one chosen before, then 
                #we can directly add it to the answer, and if the character count still remains, push it back to the heap 
                cnt+=1
                res.append(char)
            if cnt!=0:
                h.heappush(arr,(cnt,char))
        return  "".join(res)
                
                
            
    def createMapOfCharCount(self,s):
        map_ = dict(int)
        for i in s:
            map_[i]+=1  
        return map_
       