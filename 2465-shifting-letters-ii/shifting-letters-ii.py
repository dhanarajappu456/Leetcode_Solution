class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        str_ = s
        n = len(str_)
        changes = [ 0 for  i in range(n)]

        for s,e,d in shifts:
            if d ==1 :
                changes[s]+=1
                if e+1 <n :
                    changes[e+1] -=1
            else:
                changes[s] -=1
                if e+1 <n :
                    changes[e+1] += 1
     
            
        s = list(str_)
        cumul_changes = 0
        for i,c in enumerate(changes):
            cumul_changes+=c
            s[i] = chr((ord(s[i])-97+ cumul_changes)%26 + 97)
        print(s)
        return "".join(s)