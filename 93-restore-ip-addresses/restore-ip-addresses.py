class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res =[]
        n  = len(s)
        def rec(i,ans, partition ):

            if partition  ==4:
                if i ==n:
                    res.append(".".join(ans))
                    return 
            for j in range(i,min(i+3, n)):
                val = int(s[i:j+1])
                val   = int(val)
                if (val<=255 )and not(j!=i and s[i]=="0"):
                    ans.append(s[i:j+1])
                    rec(j+1,ans,partition+1)
                    ans.pop(-1)
                else:
                    break

        rec(0,[],0)
        return res      
                     
            
        


