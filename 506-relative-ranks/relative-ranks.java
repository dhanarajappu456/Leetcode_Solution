import java.util.Arrays;

class Solution {
    public String[] findRelativeRanks(int[] score) {
        Integer[] indexes = new Integer[score.length];
        for (int i = 0; i < score.length; i++) {
            indexes[i] = i;
        }

        Arrays.sort(indexes, (a, b) -> Integer.compare(score[b], score[a]));

        String[] result = new String[score.length];
        for (int i = 0; i < score.length; i++) {
            if (i == 0) {
                result[indexes[i]] = "Gold Medal";
            } else if (i == 1) {
                result[indexes[i]] = "Silver Medal";
            } else if (i == 2) {
                result[indexes[i]] = "Bronze Medal";
            } else {
                result[indexes[i]] = String.valueOf(i + 1);
            }
        }

        return result;
    }
}
