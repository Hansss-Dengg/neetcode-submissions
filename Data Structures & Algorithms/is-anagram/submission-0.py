class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted = sorted(s)
        tSorted = sorted(t)

        sJoined = "".join(sSorted)
        tJoined = "".join(tSorted)

        if(sJoined == tJoined):
            return True
        
        return False
