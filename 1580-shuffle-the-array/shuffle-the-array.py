class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        for i in range(2*n):
            curr_pos , curr_num   = i,nums[i]
            while(curr_num>0):
                if curr_pos<n: 
                #if i<n , then move the elements to 2*i the index
                    new_pos = 2*curr_pos
                    new_num = nums[2*curr_pos]
                else:
                #else , move the elemetns 2*(i-n) + 1 the index
                    new_pos = 2*(curr_pos-n)+1
                    new_num = nums[2*(curr_pos-n)+1]
                #moving the number curr_num to its intented psotion , new_pos
                #-ve sign to indicate that number intented for the position new_pos 
                # is moved that position
                
                nums[new_pos ] = - curr_num
                #the number that was at the new position , now becomes , current number
                #and its positon becomes current position 
                curr_num = new_num
                curr_pos = new_pos
 
        return [ -num for num in nums]

            