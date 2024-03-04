class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
          Arrays.sort(tokens);
        int n = tokens.length;
        int i = 0, j = n - 1;
        int score = 0;
        int ans = 0;

        while (i <= j) {
            while (i <= j && tokens[i] <= power) {
                power -= tokens[i];
                score++;
                i++;
                ans = Math.max(ans, score);
            }
            if (score >= 1) {
                power += tokens[j];
                score--;
                j--;
            } else {
                break;
            }
        }

        return ans;
    }
}