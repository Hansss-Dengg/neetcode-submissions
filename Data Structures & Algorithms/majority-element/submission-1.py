class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
                if res[num] > len(nums)/2:
                    return num
            else:
                res[num] = 1
        
        return num
        
