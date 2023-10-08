/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        let num1 = nums[i]
        let num2 = nums[i + 1]
        for (let j = i+1; j < nums.length; j++) {
            let num2 = nums[j]
            if (num1 + num2 === target) {
                return [i, j]
            } 
        }
    }
};