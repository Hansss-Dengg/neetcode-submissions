class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i, num in enumerate(nums):
            complement = target-num
            if complement in pairs:
                return [pairs[complement], i]
            pairs[num] = i 
        