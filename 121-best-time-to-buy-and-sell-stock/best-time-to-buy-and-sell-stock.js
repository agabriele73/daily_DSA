/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = Infinity
    let maxProfit = 0
    for (let i = 0; i < prices.length; i++) {
        let currPrice = prices[i]
        if (currPrice < minPrice) {
            minPrice = currPrice
        }
        let potentialProfit = currPrice - minPrice
        if (potentialProfit > maxProfit) {
            maxProfit = potentialProfit
        }
    }
    return maxProfit
};