// 


// classic matching non matching dp problem 

// when there is not match just we need to try all the possible operation 

// 


class Solution {

   
    int [][] memo;
    int m,n;   
    String word1, word2;
    public int minDistance(String word1, String word2) {
        
        
        
        this.m = word1.length();
        this.n  =  word2.length();
        this.word1 = word1; 
        this.word2 = word2; 
        this.memo =  new int[m+1][n+1];
        for(int i=0 ; i<m+1;i++ ){

            Arrays.fill(memo[i], -1);
        }

        return rec(m,n);
    


    }

    private int rec( int i, int j){

        if (i==0 || j==0){

            return  (i+j);
        }

        if(memo[i][j]!=-1 ){

            return memo[i][j];
        }
        
     

        int ans = 0;

        if (word1.charAt(i-1)== word2.charAt(j-1)){

            ans = rec(i-1,j-1); 
        }
        else{ 
            ans =  1+Math.min(Math.min(rec(i,j-1 ),rec(i-1,j)),rec(i-1,j-1) );
        }

        memo[i][j] = ans;
        return(memo[i][j]);
        // try 3 possibilities
       
    }
}