import static java.lang.Math.*;

class Solution {
    public boolean isPowerOfFour(int n) {

        if (n<=0)
            return false ;
        System.out.println( log(n)/log(4)%1 );
        return log(n)/log(4)%1 ==0 ;

        
        
    }
}