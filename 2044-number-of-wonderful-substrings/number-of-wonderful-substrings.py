'''
solution1 

approach  subarray sum  = k
we know the xor of a num even number times gives = 0 
and odd number of times gives the same number
we use this approach  to solve
we find cumulative xor and store it in map

now look how things work: 

each char a-j is mapped to vals  like 1,2,4,8....
we find the subaray ending at current index, 
a)which either has  all terms even number of times
checked by :
when at current index, we check if we have same culative xor found so far, which means that can be removed from
beginnnig
b)or either one of char from a to j  appears  odd number times
checked by 
when at current index , for each char a to j , if each of them appears exactly odd number of times
this is done by xoring this char with cumulative xor , let  call this as "prefix_to_remove", which is some 
thing that need to be cur from beginning




t 10*n = n
s  n(map)
'''
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:


        mp = dict()
        mp[0] = 1
        xor = 0 
        res = 0 
        for c in word:

            pos = ord(c)-97
            xor ^= (1<<pos)
            # to get count of subarray ending at current index,
            #with all terms even numebr of times
            if xor in mp:
                res+= mp[xor]
            val  =1 
            #getting subarray ending at current index with each char appear odd number times 
            #seperately

            while(val<= (1<<9)):
                prefix_to_remove  = xor^val
                if prefix_to_remove in mp:
                    res += mp[prefix_to_remove]
                val*=2
            mp[xor] = mp.get(xor,0)+1
            
        
        return res