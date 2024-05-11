'''
solution 1 - brute force  - w/q array + sorting 
Idea is to choose a  item  as the manager of  the grp of k items. It is based on this item's  w/q we calculate wage
Then based upon the wage/quality of this manager item we calculate the amount needed of other people
that is  amount for each other worker = manager_w/manager_q * worker_q eq -------(1)

but one condition to note is this amount given to each worker , should be >= this workers's
min_wage(let's call as worker_w)
that is manager_w/manager_q * worker_q  >= worker_w   eq -------(2)
reordering the  eq -------(2), we get  manager_w/manager_q >= worker_w /worker_q
so for a manager we can take only worker with  w/q less than this manager , so prior to bruteforcing  considering 
each item as  manager , we would need to have the w/q ratio of all elements  calculated and sorted ascending order.
also note when we calculate the ans with current element as manager  ratio(ith element) 
the ans  = curr_manager_ratio*(quality_curr_manger  + sum of k-1 smallest quality) 
This menas with current element as the manager ratio ,  we start from 0th worker item to i-1 items in the ratio array 
we keep adding thewir quality to the an arry sort this quality array and choose the least k-1 elements if there is.

t  nlogn  + n*(n+nlogn)  - sorting w/q array .Then for each element as manager ratio , we run another inner
loop from o to i-1 , to choose the least k-1 qulaity,(with w/q<= this manager ratio)
s n(ratio array)

solution 2 - optimisation - with max heap - to store the min k-1 quality of previous workers 

in solution on for each manager we statrted from beginning item in the w/q ratio array , put all of them to 
the array and sorted.
instead of this we keep on adding them to maxheap which maintins the k-1 min qualities. 
which get devoid of inner loop 

t nlogn + n*logk ( w/q sort , and run for loop considering each ratio as manager ratio  with pushing and poppoing 
from the heap of size k-1 
)
s

w/q ratio array.

manager we can only 
so essentially idea is try taking each person as manager and 
'''
import heapq as h 
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        #keeps (wage/quality, quality) for each items
        ratio = [0 for i in range(n)]
        #max_heap used to store k smalles qulities
        max_heap_quality = []
        #stores the  smallest k-1  qualities among items seen so far
        min_sum_qualities=0
        #stores the wage  per qality
        for i in range(n):
            q = quality[i]
            ratio[i] =( wage[i]  / quality[i],quality[i])
        #sorting the ratio
        ratio.sort()
        ans = float("inf")
        #iterating over the ratios in ascending order
        for i in range(n):
            curr_ratio = ratio[i][0]
            curr_qual = ratio[i][1]
            #when we have k or more items in heap we remove one items thus ensure k-1 smaller qualties are 
            #only in the heap
            
            if len(max_heap_quality)>k-1:
                #deleting the max qualities
                max_qual  = h.heappop(max_heap_quality)
                max_qual*=-1
                #removing the popped qual value from the sum_variable
                min_sum_qualities-=max_qual
            #if the total number of items >=k(k-1 smaller qualities among i elements visited so far
            #will be in heap and 1 element is the current item(manager)
            #then we can actaully start computing the ans(min amount of money needed)

            if len(max_heap_quality)==k-1:
                #assuming current items as the manager then  
                # amount needed  = manager item's wage  +  wage_up_On_qual_of_manager*(sum of k-1 qualties of previous worker items)
                
                ans  = min(ans, ratio[i][0]*min_sum_qualities + curr_ratio*curr_qual)
            #pushing current worker items quality to heap
            h.heappush(max_heap_quality,-curr_qual)
            #pushing to heap so add to the variable that keeps track of sum of k-1 elements in the heap 
            min_sum_qualities += curr_qual
        return ans 


        

        