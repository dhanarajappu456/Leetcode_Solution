'''
Solution 1 
The idea is to sort ascending by attack and then descending by defense then keep storing the max attack and 
defense as we iterate from the end.

why we need the defense to be in descending ?

If we sort both ascending and perform algo , consider test case
[[7,9],[7,12],[10,4]] when at 7,9 we will find there is one number greater than it, since max attack so far is 10 and
defense is 12, but it is no right. this happens bcz the denense 12 fall in an item with same attack 7 , which can't be 
taken so it is essentially to have the items with same attack in descending , so that 
we don't have this issue.
and sorting order then become [[7,12],[7,9],[10,4]].

t nlogn
s 1

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


        