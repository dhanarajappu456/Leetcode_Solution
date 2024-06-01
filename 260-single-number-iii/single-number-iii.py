'''

solution1 :
sorting and then comapring iadjacent to check if it occur once or twice

t nlogn 
s  1 



solution2 - using the count map

t n 
s n 



solution 3 using xor
The idea is to seperate the number that occur once into a different grp and 
finding the xor of individaul grp , ultimately will give the numbers
The  way we can do is finding xor of all nums , which is essential the xor of the
numbers that occur once.Then we can seperate them based on the first bit from right at
which they differ.
So that this ensures they would be in a different grp

t n 

s  1


'''



#solution 3
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #finding xor of all nums  = xor of nums occuring once(num1 and num2 )
        xor  = 0
        for num in nums:
            xor^= num
        bit  = 0 
        val = 1 
        #finding the first bit from right, at which the num1 and num2 have  different
        #bits
        while((val&xor) == 0):
            bit+=1
            val<<=1
        #finding xor all nums belonging to grp1 and 
        #grp2 , which is nothing but the num1 and num2 
        grp1_xor = 0
        grp2_xor = 0
        for num in nums:
            if num&val!=0:
                grp1_xor^=num
            else:
                grp2_xor^=num
        return [grp1_xor , grp2_xor]

        