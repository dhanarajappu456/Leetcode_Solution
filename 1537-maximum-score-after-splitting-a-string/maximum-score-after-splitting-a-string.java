class Solution {
    public int maxScore(String s) {
   
        int totOnes = s.replaceAll("0", "").length();
        int score = 0;
        int lZero = 0, lOne = 0;
        int n = s.length();
        
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == '0') {
                lZero++;
            } else {
                lOne++;
            }

            int rOne = totOnes - lOne;
            score = Math.max(score, lZero + rOne);
        }

        return score;
    }

 
}