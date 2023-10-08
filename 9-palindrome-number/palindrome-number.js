/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let original = x
    let reversed = 0

    while (x > 0) {
        const digit = x % 10
        reversed = reversed * 10 + digit
        x = Math.floor(x / 10)
    }
    
    return original === reversed
};