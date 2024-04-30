class Solution:
    def wonderfulSubstrings(self, word: str) -> int:


        mp = dict()
        mp[0] = 1
        xor = 0 
        res = 0 
        for c in word:

            pos = ord(c)-97
            xor ^= (1<<pos)
           
            if xor in mp:
                res+= mp[xor]
            val  =1 
            while(val<= (1<<9)):
                prefix_to_remove  = xor^val
                if prefix_to_remove in mp:
                    res += mp[prefix_to_remove]
                val*=2
            mp[xor] = mp.get(xor,0)+1
            
        
        return res