'''
[[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
'''


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_first, max_second = -1,-1
        properties.sort(key = lambda x:(x[0],-x[1]))
        cnt = 0 
        for a,b in properties[::-1]:
            if max_first>a and max_second >b :
                cnt+=1
            max_first, max_second = max(max_first, a) , max(max_second,b)
        return cnt


        