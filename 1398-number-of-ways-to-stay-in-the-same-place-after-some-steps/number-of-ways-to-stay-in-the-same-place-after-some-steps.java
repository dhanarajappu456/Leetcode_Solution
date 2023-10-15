

// approach is simple we try 3 possibilities at any index 
// the state ind, remStep is overlapping

// the state denote numb of ways to be at 0  when at ind with remStep

// t : steps * steps
// s steps * steps

class Solution {

    int mod;
    int n;
    int[][] memo;
    public int numWays(int steps, int arrLen) {
        this.mod = 1000000007;
        this.n = arrLen;
        this.memo = new int[steps+1][steps+1];
        
   
        for(int i=0;i<steps+1;i++){
              Arrays.fill(memo[i],-1);
            
            
        }
    

        return rec(0,steps);
        
    }


    private int rec(int ind, int remStep) {
    if (remStep == 0) {
        return (ind == 0) ? 1 : 0;
    }

    if (ind < 0 || ind >= n) {
        return 0;
    }

    if (memo[ind][remStep] != -1) {
        return memo[ind][remStep];
    }

    int r = rec(ind + 1, remStep - 1) % mod;
    int s = rec(ind, remStep - 1) % mod;
    int l = rec(ind - 1, remStep - 1) % mod;
    // remember to apply mod at each step,else get the overflow
    memo[ind][remStep] = ((r + s) % mod + l) % mod;

    return memo[ind][remStep];
}
}
