class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def merge(arr,l,m,h):
    
            temp = []

            i,j,k = l,m+1,0

            while(i<=m and j<=h):

                if arr[i]<= arr[j]:

                    temp.append(arr[i])
                    i+=1
                    k+=1
                else:
                    temp.append(arr[j])
                    j+=1
                    k+=1
            while(i<=m):


                temp.append(arr[i])
                i+=1
                k+=1


            while(j<=h):

                temp.append(arr[j])
                j+=1
                k+=1

   
            for i in range(l,h+1):
                arr[i] = temp[i-l]

        def mergeSort(arr,l,h):

            if l==h:
                return 
            m  =  (l+h)//2

            mergeSort(arr,l,m)
            mergeSort(arr,m+1,h)
            #merge the sorted left and right half - takes approx(o(n))
            merge(arr,l,m,h)
        n = len(nums)
        mergeSort(nums,0,n-1)
        return nums

        