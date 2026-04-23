class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        values = {}
        for num in nums:
            if num in values:
                values[num] = values[num] + 1
            else:
                values[num] = 1
        res = nums[0]
        for num in values:
            if values[num] == 1:
                res = num
        
        return res
            
