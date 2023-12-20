class Solution {
    public int buyChoco(int[] prices, int money) {
        int min_1 = Integer.MAX_VALUE;
        int min_2 = Integer.MAX_VALUE;
        int n = prices.length;

        for (int i = 0; i < n; i++) {
            if (prices[i] <= min_1) {
                min_2 = min_1;
                min_1 = prices[i];
            } else if (prices[i] < min_2) {
                min_2 = prices[i];
            }
        }

        int left = money - (min_1 + min_2);
        if (left < 0) {
            return money;
        }
        return left;
    }
}