class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stk  = []
        i =   0
        n  = len(formula)

        def getTheAtomAndCount():
            nonlocal i
            a = []
            a.append(formula[i])
            i+=1 
            while(i<n and formula[i].isalpha() and formula[i].islower()):
                a.append(formula[i])
                i+=1
            num  = 1 
            if i<n and formula[i].isnumeric() :
                num = ""
                while(i<n and formula[i].isnumeric()):
                    num += formula[i]
                    i+=1
                num = int(num)
            atom = "".join(a)
          
            return atom , num




        while(i<n):

            c = formula[i]
            if c == "(":
                stk.append(defaultdict(int))
                i+=1
            elif c.isalpha():
                atom, num =  getTheAtomAndCount()
                if not stk:
                    stk.append(defaultdict(int))
                stk[-1][atom]=  stk[-1][atom]+ num


            elif c ==")":
                i+=1
                num  = 1 
                if i<n and formula[i].isnumeric() :
                    num = ""
                    while(i<n and formula[i].isnumeric()):
                        num += formula[i]
                        i+=1
                num = int(num)
                dt = stk.pop(-1)
                for val in dt:
                    dt[val] = dt[val]*num
                if stk:
                    for val in dt:
                     
                        stk[-1][val] += dt[val]
                else:
                    stk.append(dt)
        atoms  = list(stk[-1].keys())
        atoms.sort()
        ans  =""
       
        for k in atoms:
          
            ans+= k+ (str(stk[-1][k]) if stk[-1][k] > 1 else "")
        return ans
            




        