/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    
    

    function countBits(num){
       let cnt = 0;
        while (num) {
            num = num & (num - 1);
            cnt++;
        }
        return cnt;

    }
    arr.sort((a,b)=>{
        const aBit =countBits(a) 
        const bBit = countBits(b)
        if( aBit!==bBit){

            return aBit-bBit
        }


        return a-b;
    })
    return arr; 
};