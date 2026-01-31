class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        
        int n = letters.length;
        int i = 0;
        for( i = 0 ;i<n; i++){
            
            char c  = letters[i];

            if (c > target){
                 break;
            }
            
              

        }


        return i<n ? letters[i] : letters[0];
    }
}