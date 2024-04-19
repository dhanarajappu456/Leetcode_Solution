'''
the idea is, starting form bottom , we need to find actual parent to which the current label migh have
connected to , then find the posiiton of this parent in the level it is present , denoted by position_from_end 
this value need to be added to value of  starting node of the level. this is repeated
t logn
s aux(logn)
'''
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
    
        ans =[]
        ans.append(label)
        while label>1:
            #actual parent
            actual_par = label//2
            #finding prev level (first level =0 )
            prev_level = int(math.log(actual_par,2))
            #finding max value in the prev level
            max_in_prev_level = 2**(prev_level+1)-1
            #finding the position of actual parent in the level(from right side)
            position_from_end = max_in_prev_level - actual_par
            #now this initial positio value to be added to the starting value of the level
            #to get actual position
            res  = ( 2**prev_level)+position_from_end
            ans.append(res)
            label =res
        #ans need to be reversed 
        return ans[::-1]