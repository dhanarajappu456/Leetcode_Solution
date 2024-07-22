class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h =[(height,i) for i,height in enumerate(heights)]
        h.sort(reverse  = True)
        ans = []
        print(h)

        ans =[names[ind] for i,(ht,ind) in enumerate(h)]

        return ans 
        