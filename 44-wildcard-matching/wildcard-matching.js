/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {

    memo = {}
    function rec(i,j){
        
      
        if(j=== 0){
            
            return (i===0);
        }
        else if(i===0){

            for(let k=1 ; k<=j; k++){
                
                if (p[k-1]!=="*") {
                    return false;
                }


            }
        return true;

                

        }

        if( [i,j] in memo){

                return memo[[i,j]];
        }

        let ans = false;
 
        if (p.charAt(j-1)==='?' || (s.charAt(i-1) === p.charAt(j-1))){
            console.log("equal / ? ", i,j)
            ans =  rec(i-1, j-1);

        }

        else if(p.charAt(j-1) === "*"){
            
            ans =  ( rec(i-1,j) || rec(i, j-1) ); 

        }


         memo[[i,j]]  = ans;
         return ans

    }

    return rec(s.length , p.length);
    
};