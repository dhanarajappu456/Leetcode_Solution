/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumScore = function(nums, k) {

    n = nums.length
    prevSmall = Array(n).fill(0)
    nextSmall = Array(n).fill(0)
    stk =[[-1,-1]]
    for(let i = 0 ;i<nums.length ;i++){

        num  = nums[i]
        while(stk.length>0  && stk[stk.length-1][1]>= num){


            stk.pop()
        }
        
        prevSmall[i] = stk[stk.length-1][0]
        stk.push([i,num])

    }
        
    stk =[[n,-1]]
    for(let i= nums.length-1;i>=0 ; i--){

        num  = nums[i]
        
        while(stk.length>0 &&  stk[stk.length-1][1]>= num){
            stk.pop()
        

        }
            
        nextSmall[i] =  stk[stk.length-1][0]
        stk.push([ i,num])
    }
        
    let ans =  nums[k]
    for(let p = 0; p<nums.length;p++){
        num  = nums[ p]
        i = prevSmall[p]+1
        j = nextSmall[p]-1
        //if the subarray is good subarray , take the score into accounte 
        if (i<=k && k<=j){
            ans =Math.max(ans, num *(j-i+1))

        }
    }
            
    return ans
    
};