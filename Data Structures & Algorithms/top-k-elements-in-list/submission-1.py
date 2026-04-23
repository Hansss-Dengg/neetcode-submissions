class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        kMostCommon = counts.most_common(k)
        return[num for num, k in kMostCommon]