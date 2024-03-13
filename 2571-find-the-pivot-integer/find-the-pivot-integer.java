public class Solution {
    public int pivotInteger(int n) {
        // Calculate the total sum of the sequence 1...n
        int tot = n * (n + 1) / 2;

        // Iterate over the sequence 1...n
        for (int i = 1; i <= n; i++) {
            // Check if the current element is equal to the square root of tot
            if (i == Math.sqrt(tot)) {
                return i; // If true, return the element
            }
        }
        return -1; // If no such element found, return -1
    }
}