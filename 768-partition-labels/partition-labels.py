class Solution:
    def partitionLabels(self, s: str) -> List[int]:
  
        d = defaultdict(int)
        for (i,c) in enumerate(s):
            d[c] = i
        ans  = [ ]
        i = 0 
        n = len(s)
        while(i<n):
            c  = s[i]
            last_ind  = d[c] 
            k = i
            while(k<n and k!=last_ind):
                last_ind = max(last_ind , d[s[k]])
                k +=1 
            ans.append(last_ind-i+1)
            i  = last_ind + 1 
        return ans
        