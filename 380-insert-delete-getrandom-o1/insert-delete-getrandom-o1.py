'''
solution 1 

with list + dict 


the idea to use the list to store the inserted number 
for faster lookup we need a set or dict 

but problems is with remove , since remove is o(N) in li, rather than removinng the number from random index we swap with last number and delte from end 

but to get ind of val to be deleted , we maintain the dict that map val to ind

t o(1) each op
s n 

'''
from collections import defaultdict as dict 

class RandomizedSet:

    def __init__(self):

        self.li = []
        self.mp = dict(list)
        

    def insert(self, val: int) -> bool:

        if val not in self.mp:
            
            self.li.append(val)
            self.mp[val] = len(self.li)-1 
            return True
        return False
        

    def remove(self, val: int) -> bool:

        if val in self.mp:
            ind = self.mp[val]
            self.li[ind] = self.li[-1]
            self.mp[self.li[-1]] =ind
            self.li.pop(-1)
            del self.mp[val]
            return True
        return False
        

    def getRandom(self) -> int:

        return random.choice(self.li)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()