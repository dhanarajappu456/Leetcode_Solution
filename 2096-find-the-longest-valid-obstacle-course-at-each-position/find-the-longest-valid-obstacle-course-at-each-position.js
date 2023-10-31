/**
 * @param {number[]} obstacles
 * @return {number[]}
 */
var longestObstacleCourseAtEachPosition = function(obstacles) {
    nums = obstacles 
    n = nums.length
    const lis  =[]
    const dp = Array(n).fill(1)


    function binSearch(lis,i){

       
            const num = nums[i]
            let ans  = -1
            let s= 0,e = lis.length-1
            while(s<=e){

                m  = (s+e)//2
                if( lis[m]<=num){

                    ans = m 
                    s =m+1
                }
                else{
 
                    e = m-1

                }
                  
                   



            }
              

            return ans+1


    }
     
     nums.forEach((num ,i)=>{

            ind =binSearch(lis , i) 
            dp[i] = ind+1 
            if (ind>=lis.length){ lis.push(num)}
               
            else{

             lis[ind] = num
            }
               
         
            

     })
                
       
        return dp
};