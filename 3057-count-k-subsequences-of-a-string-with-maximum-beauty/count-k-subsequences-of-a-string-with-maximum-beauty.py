import math
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
       
    
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
        print(mp)
        if k>len(seen):
            return  0 
        for freq   in sorted(mp.keys(),reverse = True):
            if remain ==0 :
                break
       
            if mp[freq]<=remain:
                print( (freq**mp[freq]))
                res *= (freq**mp[freq])
                remain-= (mp[freq])
            
            else:
                print("combi",mp[freq],remain,math.comb(mp[freq],remain))
                combi   = (freq**remain)*math.comb(mp[freq],remain)
                print(combi,id(combi))
                break
        #print(combi,res,id(combi))
        ans = (combi*res)%MOD
        
        return ans
            