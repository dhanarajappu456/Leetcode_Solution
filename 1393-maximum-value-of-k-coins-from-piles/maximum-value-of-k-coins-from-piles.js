/**
 * @param {number[][]} piles
 * @param {number} k
 * @return {number}
 */


var maxValueOfCoins = function(piles, k) {

    const n  = piles.length ;

    const memo = {}


    function rec(ind , k){


        if(ind===n || k ===0){

            return 0;
        }

        const key  = [ind,k ].toString()

        if( key in memo){

            return memo[ key ]
        } 
        // not take


        let   ans = 0 


        ans = Math.max(ans ,   rec(ind+1, k))
        let  currPileCoin =0 

        for(let i = 0 ; i<Math.min(k,piles[ind].length); i++){

                currPileCoin += piles[ind][i]
               
ans = Math.max(ans, currPileCoin + rec(ind + 1, k-(i+1)));

            }


        

        memo [  key ] =  ans
  
        return ans




    }


    return rec(0 , k)


};