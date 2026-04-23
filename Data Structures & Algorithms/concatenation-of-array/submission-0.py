class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        result = [0] * (len(nums)*2)
        for i,num in enumerate(nums):
            result[i] = result[i+len(nums)] = num
        
        return result