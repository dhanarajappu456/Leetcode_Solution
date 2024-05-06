class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        pref  = [0 for i in range(n+1)]
        pref_pref =[0 for i in range(n+2)]

        for i in range(n):
            num = strength[i]
            pref[i+1] = pref[i]+num

        for i in range(1,n+1):
            num = pref[i]

            pref_pref[i+1] = pref_pref[i] + num
   

        stk =[]
        prev_sm = [0 for i in range(n)]
        for i,num in enumerate(strength):
            while(stk and strength[stk[-1]]>num):
                stk.pop(-1)
            prev_sm[i] = stk[-1]  if stk else -1
            stk.append(i)

      

        stk =[]
        next_sm = [0 for i in range(n)]
        for i,num in reversed(list(enumerate(strength))):
            while(stk and strength[stk[-1]]>=num):
                stk.pop(-1)
            next_sm[i] = stk[-1]  if stk else n
            stk.append(i)

        

        ans  = 0
        mod = 10**9+7
        for i , num in enumerate(strength):
            curr_min = num
            l,r  = prev_sm[i]+1,next_sm[i]-1 
        
            val = ((pref_pref[r+2]- pref_pref[i+1])*(i-l+1) - (pref_pref[i+1]- pref_pref[l])*(r-i+1))  *curr_min
            ans = (ans%mod + (val%mod))%mod
            
        return ans



        