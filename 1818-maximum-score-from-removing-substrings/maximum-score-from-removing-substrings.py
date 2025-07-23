class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def remove_s(st,rm):
            ans  = ""
            stk  = []
            for c in st:
                if (stk and ( stk[-1] == rm[0] ) and (c == rm[1])):
                    stk.pop(-1)
                else:
                    stk.append(c)
       
            ans = "".join(stk)
            return ans
    
        n = len(s)
        res = 0 
        max_str =    "ab"  if x > y  else  "ba"
        min_str =    "ab"  if x<=y   else  "ba"
        str1 = remove_s(s,  max_str)
        res  = (n-len(str1))//2 * (x if max_str =="ab" else y )

        str2 = remove_s(str1, min_str)
      
        res += (len(str1)-len(str2))//2 * (x if min_str =="ab" else y )
        return res