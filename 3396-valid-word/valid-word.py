class Solution:
    def isValid(self, word: str) -> bool:
        vows = set(["a","e","i","o","u","A","E","I","O","U"])
        nums = set(["0","1","2","3","4","5","6","7","8","9"])
        def check(word):
            dig = 0 
            vow  =  0
            cons = 0 
            for c in word:
                if c in vows:
                    vow+=1
                elif ( 0 <= ( ord(c) - ord('a') ) <= 26):
                    cons+=1
                elif ( 0 <= ( ord(c) - ord('A') ) <= 26):
                    cons+=1
                elif c in nums:
                    dig+=1
                else:
                    print("haai")
                    return False
        
            if (vow>=1) and (cons>=1 )and (len(word)>=3):
                return True
            return False
        return check(word)
   

        

            