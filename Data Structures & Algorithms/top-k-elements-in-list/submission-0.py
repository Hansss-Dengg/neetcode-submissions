class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        kMostFrequent = counts.most_common(k)
        return[num for num, freq in kMostFrequent]