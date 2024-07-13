class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        survived = set()
        n  = len(healths)
        info  = [[positions[i] , healths[i], directions[i], i ] for i in range(n)]
        info.sort(key =  lambda x: x[0])
        
        stk =[]
        print(info)
        for curr_ind, ( curr_pos, curr_hel, curr_dir,old_ind) in enumerate(info):
        
            eq  = False 
    
            while stk and info[stk[-1]][2]=="R" and  info[curr_ind][2]=="L" :
                top = stk.pop()
                if info[top][1]>info[curr_ind][1]:
                    info[top][1]-=1
                    info[curr_ind][1] = None
                    curr_ind =  top 
                elif info[top][1]<info[curr_ind][1]:
                    info[top][1] = None
                    info[curr_ind][1] -=1 
                else:
                    info[top][1] = None
                    info[curr_ind][1]  = None
                    eq = True
                    break
            if not (eq):
               stk.append(curr_ind)
           
        info.sort(key =  lambda x: x[3])
        return [item[1] for item  in info  if item[1] != None ]
        