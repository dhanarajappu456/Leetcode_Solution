class Solution {
    public int largestSubmatrix(int[][] matrix) {
        

         int m = matrix.length;
        int n = matrix[0].length;
        int[] heights = new int[n];
        int maxArea = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    heights[j] = 0;
                } else {
                    heights[j] += 1;
                }
            }

            int[] sortedHeights = Arrays.copyOf(heights, n);
            Arrays.sort(sortedHeights);

            for (int j = 0; j < n; j++) {
                int h = sortedHeights[j];
                int area = h * (n - j);
                maxArea = Math.max(area, maxArea);
            }
        }

        return maxArea;

  
    }
}



