class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}

        for i,num in enumerate(nums):
            complement = target-num
            if complement in results:
                return [results[complement], i]
            results[num] = i

    
        return []