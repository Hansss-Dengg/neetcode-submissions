class Solution:
    def isPalindrome(self, s: str) -> bool:
        sUpper = s.upper()
        p1 = 0
        p2 = len(s)-1

        while p1<=p2:
            if sUpper[p1].isalnum() and sUpper[p2].isalnum() and sUpper[p1]!=sUpper[p2]:
                return False
            elif not sUpper[p1].isalnum():
                p1+=1
            elif not sUpper[p2].isalnum():
                p2-=1
            else:
                p1+=1
                p2-=1
        
        return True



