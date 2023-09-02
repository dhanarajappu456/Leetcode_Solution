import math
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
       
        #create map of count mapped to number of charcter having that counr
        #choose the k unique charcter having the max coutn 
        #remember sometimes, we migh end up choosing only some numbers from a character of particular count ,in that case , we might need combination to choose those character
        mp ={}
        seen  = set()
        MOD = 10**9+7 
        
    
        for c in s:
            if c not in seen :
                
                seen.add(c)
                mp[s.count(c)] = mp.get(s.count(c),0)+1
        
      
        remain = k
        combi =1 
        res= 1

        #if k> number of unique character in the string , no possibility to form , the required beauty subsequence 
        if k>len(seen):
            return  0 
        for freq   in sorted(mp.keys(),reverse = True):
            if remain ==0 :
                break
            #choosing all the leeters of this freq 
            if mp[freq]<=remain:
                print( (freq**mp[freq]))
                res *= (freq**mp[freq])
                remain-= (mp[freq])
            
            #end up choosing some chars from chars of particular count
            else:
            
                combi   = (freq**remain)*math.comb(mp[freq],remain)
            
                break
      
        ans = (combi*res)%MOD
        
        return ans
            