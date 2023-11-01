class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 1: 
            return nums[0]

        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        for x in count_dict:
            if count_dict[x] == 1:
                return x
        
        