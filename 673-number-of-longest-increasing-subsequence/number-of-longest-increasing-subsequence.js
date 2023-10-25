/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumberOfLIS = function(nums) {

    n = nums.length;
    const dpLis  = Array(n).fill(1);
    const dpLisCount = Array(n).fill(1);
    
    for(let i=0 ;i<n;i++){

        let j= i-1; 
        while(j>=0){
            if(nums[j]< nums[i]){
                if(dpLis[i]<1+dpLis[j]){

                    dpLis[i] = 1+dpLis[j]
                    dpLisCount[i]=0
                    dpLisCount[i] += dpLisCount[j]


                }
                else if(dpLis[i]===1+dpLis[j]){
                    dpLisCount[i] +=dpLisCount[j]

                }
           
            }
            
            j-=1
        }
       

    }
    // console.log(dpLis,dpLisCount)
    return dpLisCount.reduce((acc, val,ind)=>{

                if (dpLis[ind] === Math.max(...dpLis)){

                    return acc+ val;
                }
                else{
                    return acc;
                }


    },0 );


    
    
};