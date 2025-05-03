class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        mx_top_val, mx_top_cnt =  Counter(tops).most_common(1)[0][0] , Counter(tops).most_common(1)[0][1]
        mx_bottom_val, mx_bottom_cnt = Counter(bottoms).most_common(1)[0][0] , Counter(bottoms).most_common(1)[0][1]
        
        arr3 = []
        arr4 = [] 
        max_val2  = 0
        def check(arr1,arr2, max_val):

            for i in range(len(arr1)):
                if arr1[i] != max_val:
                    if arr2[i]!=max_val:
                        return False
            return True

        if mx_top_cnt > mx_bottom_cnt :
            arr1 = tops
            arr2 = bottoms
          
            max_cnt  = mx_top_cnt
            max_val  = mx_top_val
            if check(arr1, arr2, max_val):
                return len(arr1) - max_cnt
          
        elif mx_top_cnt < mx_bottom_cnt:
            arr1 = bottoms
            arr2 = tops
            max_cnt = mx_bottom_cnt
            max_val = mx_bottom_val   
            if check(arr1, arr2,max_val):
                print("bottoms")
                return len(arr2) - max_cnt 

    
        else: 
            arr1 = bottoms
            arr2 = tops
            max_cnt = mx_bottom_cnt
            max_val = mx_bottom_val   

            if check(arr1, arr2 , max_val):
                return len(arr1) - max_cnt


            arr1 = tops
            arr2 = bottoms
            max_cnt = mx_top_cnt
            max_val = mx_top_val   

            if check(arr1, arr2, max_val):
                return len(arr1) - max_cnt
        
        return -1 




        



      