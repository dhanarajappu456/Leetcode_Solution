/**
 * @param {number[]} prices
 * @param {number} money
 * @return {number}
 */
var buyChoco = function(prices, money) {
    
        let min_1 = Number.POSITIVE_INFINITY;
        let min_2 = Number.POSITIVE_INFINITY;
        const n = prices.length;

        for (let i = 0; i < n; i++) {
            if (prices[i] <= min_1) {
                min_2 = min_1;
                min_1 = prices[i];
            } else if (prices[i] < min_2) {
                min_2 = prices[i];
            }
        }

        const left = money - (min_1 + min_2);
        if (left < 0) {
            return money;
        }
        return left;
};