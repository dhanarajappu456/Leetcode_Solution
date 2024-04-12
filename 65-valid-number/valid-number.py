class Solution:
    def isNumber(self, s: str) -> bool:
        def is_int(s,canbe_signed):
            print('lol',s,canbe_signed)
            chars = set(s)
            if len(s)==0:
                return False
            if not(canbe_signed) and (s.count("+") >0 or s.count("-")>0)  :
                return False
            
            #no decimals, or e or more than 1 ,+ or - 
            if "." in chars or "e" in chars or s.count("-")>1 or s.count("+")>1 :
                return False
            #if + is there then 0 chould nt be there
            #case need to handle proper signed numbers(true) and +inf(false)
            if s[0]=="+" :
                return len(s)>1 and( "-" not in chars) and  "".join(s[1:]).isdigit()
            #if - there + shouldnt be there
            #case need to handle proper signed numbers(true) and -inf(false)
            if s[0] =="-":
                return len(s)>1 and( "+" not in chars) and  "".join(s[1:]).isdigit()
            if "+" in s:
                return False
            if "-" in s:
                return False

            return "".join(s).isdigit()
           
        def is_dec(s):
            
            chars = set(s)
            if len(s)==0:
                return False
            #if . in the number split and check
            if s.count(".") ==1:
                #t = is_int(s[:s.index(".")],True) and is_int(s[s.index(".")+1:],False) 
             
                #wither leeft or right side must be integer
                #eg -.1  and -1. are valid  dec according to question 
                
                for i, c in enumerate(s):
                    if c in "abcdefghijklmnopqrstuvwxyz":
                        return False
                    if i!=0 and (c=="+" or c=="-"):
                        return False
                 
                return (  is_int(s[:s.index(".")],True)  or   is_int(s[s.index(".")+1:],False) )  
                 
                
            return False
        

        def is_exp(s):
            chars = set(s)
            if len(s)==0:
                return False
            #if e in the number split and check
            if s.count("e") ==1:
                print( (is_dec(s[:s.index("e")]) or is_int(s[:s.index("e")],True)) and is_int(s[s.index("e")+1:],True) )
                return (is_dec(s[:s.index("e")]) or is_int(s[:s.index("e")],True)) and is_int(s[s.index("e")+1:],True) 
            return False
        
        
      

        s = [c.lower() for c in s ]
        
        return  is_int(s,True) or is_dec(s) or is_exp(s) 
        return False
      


        