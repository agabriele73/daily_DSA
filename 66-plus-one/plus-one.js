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

    for (let i = n - 1; i>= 0; i--) {
        digits[i]++ 

        if (digits[i] === 10) {
            digits[i] = 0;
        } else {
            return digits
        }
    }

    digits.unshift(1)

    return digits

    
};