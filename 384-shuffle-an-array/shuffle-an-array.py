'''
#solution 1 -bruteforc

t n^2
s n(temp used to restore the array)
#solution2 - fisher yates - algo

'''
#solution 2

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.temp = nums.copy()
    
      
        

    def reset(self) -> List[int]:
        
        self.nums = self.temp.copy()
      
        return self.nums
        

    def shuffle(self) -> List[int]:
        
        n = len(self.nums)
        arr = self.nums[:]
        for i in range(n):
            rand_ind  = random.randint(i,n-1)
            self.nums[i],self.nums[rand_ind] = self.nums[rand_ind],self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()