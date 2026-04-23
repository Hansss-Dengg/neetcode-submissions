class Solution:
    def isValid(self, s: str) -> bool:
        bracketClosed = 0
        squiggleClosed = 0
        squareClosed = 0

        stack = deque()
        for c in s:
            if(c == '(' or c=='{' or c=='['):
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if(c == ')' and top != '('):
                    return False
                if(c == '}' and top != '{'):
                    return False
                if(c == ']' and top != '['):
                    return False
        
        

        return len(stack) == 0
        