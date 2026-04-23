class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0
        mySet = set(nums)
       

        for num in mySet:
            if num-1 not in mySet:
                length = 0
                while num + length in mySet:
                    length += 1
                if length > max:
                    max = length
          
        
        return max

            