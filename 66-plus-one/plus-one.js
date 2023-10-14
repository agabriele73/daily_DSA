/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    // let joinedD = digits.join('')

    // joinedD++ 

    // let stringNum = joinedD.toString()
    // let numsArr = stringNum.split('')

    // let result = numsArr.map(i=>Number(i))

    // return result

    const n = digits.length;
    // Traverse the digits array from right to left
    for (let i = n - 1; i>= 0; i--) {
        digits[i]++ 
    // If the current digit becomes 10, set it to 0 and continue to the next digit
        if (digits[i] === 10) {
            digits[i] = 0;
        } else {
             // If the current digit is not 10, there's no carry, so we can stop here.
            return digits
        }
    }
    // If we reach this point, it means the entire number was 9s, and we need to add a new digit (1) at the beginning
    digits.unshift(1)

    return digits

    
};