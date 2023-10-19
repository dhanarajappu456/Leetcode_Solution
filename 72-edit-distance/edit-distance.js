
// 


// classic matching non matching dp problem 

// when there is not match just we need to try all the possible operation 

// 

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    const m = word1.length ,n= word2.length;    
    const memo = Array.from({length: m+1}, ()=>{return Array(n+1).fill(-1)})

    function rec( i,j) {

        if (i===0 || j===0){

            return  (i+j);
        }

        if(memo[i][j]!=-1 ){

            return memo[i][j];
        }
        
     

        let ans= 0;

        if (word1.charAt(i-1)=== word2.charAt(j-1)){

            ans = rec(i-1,j-1); 
        }
        else{ 
                   // try 3 possibilities
            ans =  1+Math.min(rec(i,j-1 ),rec(i-1,j), rec(i-1,j-1) );
        }

        memo[i][j] = ans;
        return(memo[i][j]);

 
       
    }

    return rec(m, n);

    
};

