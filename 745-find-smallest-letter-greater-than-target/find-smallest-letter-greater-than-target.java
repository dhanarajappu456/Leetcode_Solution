import java.util.Arrays;

class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int idx = Arrays.binarySearch(letters, target);

        // If found, skip all duplicates
        if (idx >= 0) {
            while (idx < letters.length && letters[idx] == target) {
                idx++;
            }
        } else {
            // target not found → get insertion point
            idx = -idx - 1;
        }

        // wrap-around if target >= all letters
        return letters[idx % letters.length];
    }
}

