class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
    
        ans =[]
        ans.append(label)
        while label>1:
            actual_par = label//2
            prev_level = int(math.log(actual_par,2))
            max_in_prev_level = 2**(prev_level+1)-1
            diff = max_in_prev_level - actual_par
            res  = ( 2**prev_level)+diff
            ans.append(res)
            label =res
        return ans[::-1]