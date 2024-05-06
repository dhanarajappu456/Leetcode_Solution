'''
using monotonic prevsmall and next small
the idea is to understand find the sum of all the subarrays for current element as the minimum element in the 
subarrays

for this we need to find the prev small elements index  and next small  elements index , which can be done 
with monotonic stack

when finding all the subarray with current element as the min , using this we also might need the snd degree prefix sum
which is prefix sum array of prefixsum array. 

the idea for this is got by rearranging the formula

suppose l, is  indez towards left where all elemtns> current num  
and r is index  last index towrds which all elements>= current num 

from this we get  the sum of subarray with current element as min element

pref[i]- pref[l-1] +
pref[i+1]- pref[l-1] +
.
.
pref[r]- pref[l-1] +

+ 

pref[i]- pref[l] +
pref[i+1]- pref[l] +
.
.
pref[r]- pref[l] +

+

pref[i]- pref[i-1] +
pref[i+1]- pref[i-1] +
.
.
pref[r]- pref[l-1] +


which can be simplified as 
(pref[i] + pref[i+1] + ... pref[r] )*(i-l+1) +
(pref[l-1] + pref[l] + ... pref[i-1] )*(r-i+1)

to find the sum of these subarray from pref in o(1) we need pref sum array for thie pref array
t n
s n
'''
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        #prefix sum
        #pref sum till strength[i] is in pref[i+1]
        pref  = [0 for i in range(n+1)]
        #prefix of prefix sum
        #pref sum till pref[i] is in pref_pref[i+1]
        pref_pref =[0 for i in range(n+2)]

        for i in range(n):
            num = strength[i]
            pref[i+1] = pref[i]+num
        #we need pref_pref array in calulation , here we find this array from the pref array 
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
        #calculating the ans , where current element is the min element in the subarrays

        for i , num in enumerate(strength):
            curr_min = num
            l,r  = prev_sm[i]+1,next_sm[i]-1 
            #note that pref sum of pref sum till index k in strength array is  at index k+2 in pref_pref array
            val = ((pref_pref[r+2]- pref_pref[i+1])*(i-l+1) - (pref_pref[i+1]- pref_pref[l])*(r-i+1))  *curr_min
            ans = (ans%mod + (val%mod))%mod
            
        return ans



        