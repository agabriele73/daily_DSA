/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    
    let numSet = new Set()

    for (let num of nums) {
        if (numSet.has(num)) {
            return true
        } else {
            numSet.add(num)
        }
    }
    return false
}