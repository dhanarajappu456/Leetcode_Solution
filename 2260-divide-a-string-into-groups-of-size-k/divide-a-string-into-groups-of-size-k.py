class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n =len(s)
        part = math.ceil(n/k)
        i = 0
        ans  =  []
        while(part):
            if part==1:
                if i+k>n:
                    ans.append(s[i:i+k]+fill*(k-(n-(i))))
                else:
                    ans.append(s[i:i+k]) 
            else:
                ans.append(s[i:i+k])
            i = i+k
            part-=1
        return ans


        