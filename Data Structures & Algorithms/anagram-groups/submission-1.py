class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            sortedWord = "".join(sorted(word))
            anagram_groups[sortedWord].append(word)
        
        return list(anagram_groups.values())