class Solution:
    def isValid(self, s: str) -> bool:

        smap = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []
        if len(s) <= 1:
            return False

        for char in s: 
            if char in smap:
                stack.append(char)
            else:  
                if not stack:
                    return False
                opening = stack.pop()
                if smap[opening] != char:
                    return False

        return True if len(stack) == 0 else False